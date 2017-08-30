import datetime, time, requests, pytz
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from settings import CLIENT_ID, CLIENT_SECRET_ID
from .forms import PatientForm, DemographicsForm
from .models import Doctor, Patient
from .utils import API_request, create_patient_database#, update_wait_time

# Create your views here.
def auth(request):

	response = requests.post('https://drchrono.com/o/token/', data={
		'code': request.GET['code'],
    	'grant_type': 'authorization_code',
    	'redirect_uri': 'http://0.0.0.0:8000/auth',
    	'client_id': CLIENT_ID,
    	'client_secret': CLIENT_SECRET_ID,
	})

	response.raise_for_status()
	data = response.json()

	request.session['access_token'] = data['access_token']

	user_data = API_request('https://drchrono.com/api/users/current', data['access_token'])

	user, created = Doctor.objects.get_or_create(username=user_data['username'])
	user.access_token = data['access_token']
	user.refresh_token = data['refresh_token']
	user.token_expiration = datetime.datetime.now(pytz.utc) + datetime.timedelta(seconds=data['expires_in'])
	user.save()

	request.session['doctor'] = user_data['username']

	return HttpResponseRedirect(reverse('landing'))

def landing(request):
	return render(request, 'landing.html')

def dashboard(request):

	doctor = Doctor.objects.get(username=request.session['doctor'])
	completed_appointment = request.POST

	if completed_appointment:
		patient = Patient.objects.get(pid=completed_appointment['pid'], status="In Session")
		total_wait_time = doctor.avg_wait_time * doctor.patients_seen + patient.wait_time
		doctor.avg_wait_time = total_wait_time / (doctor.patients_seen + 1)
		doctor.patients_seen += 1
		doctor.save()

	return render(request, 'dashboard.html', {'doctor' : doctor})


def show_patients(request):
	utc_time = datetime.datetime.utcnow()
	tz = pytz.timezone('US/Pacific')

	status_change = request.POST
	patients = Patient.objects.all()

	if status_change:
		checkedin_patient = Patient.objects.get(pid=status_change['pid'])
		checkedin_patient.status = status_change['status']

		if checkedin_patient.status == "Arrived":
			checkedin_patient.checkin_time = datetime.datetime.now()
		checkedin_patient.save()

	elif not patients:
		create_patient_database(request, utc_time, tz)

	arrived_patients = Patient.objects.filter(status="Arrived")
	
	for patient in arrived_patients:
		time_diff = datetime.datetime.now() - patient.checkin_time.replace(tzinfo=None)
		patient.wait_time = time_diff.seconds / 60
		patient.save()

	appointments = Patient.objects.all()

	return render(request, 'show_patients.html', {'appointments': appointments})

def checkin(request):
	form = PatientForm()

	return render(request, 'checkin.html', {'form': form})

def get_patient(request):

	form = PatientForm(request.POST)

	if form.is_valid():
		first_name = form.cleaned_data['first_name']
		last_name = form.cleaned_data['last_name']
	else:
		return render_to_response('checkin.html', {'form': form }, RequestContext(request))

	patients = []
	patients_url = 'https://drchrono.com/api/patients?first_name=' + first_name + '&last_name=' + last_name
	
	while patients_url:
		data = API_request(patients_url, request.session['access_token'])
		patients.extend(data['results'])
		patients_url = data['next']

	
	db_patients = Patient.objects.filter(first_name=first_name, last_name=last_name)
	if not db_patients.exists():
		return render(request, 'get_patient.html', {'patients': patients})

	return render(request, 'get_patient.html', {'patients': db_patients})


def demographics(request):

	pid = request.POST.get('id')
	request.session['id'] = pid
	patient = API_request('https://drchrono.com/api/patients/' + str(pid), request.session['access_token'])

	request.session['initial'] = {'social_security_number': patient['social_security_number'],
										'date_of_birth': patient['date_of_birth'],
										'gender': patient['gender']}

	form = DemographicsForm(initial = request.session['initial'])

	return render(request, 'demographics.html', {'form': form, 'id': pid})

def update_demographics(request):
	
	form = DemographicsForm(request.POST, initial=request.session['initial'])
	
	data = {}
	if form.is_valid() and form.has_changed():
		for field in form.changed_data:
			data[field] = form.cleaned_data[field]
	
	response = requests.patch('https://drchrono.com/api/patients/' + request.POST.get('id'), headers={
    'Authorization': 'Bearer %s' % request.session['access_token']}, data=data)

	return HttpResponseRedirect(reverse('allset'))

def allset(request):
	
	req = HttpRequest()
	req.method = 'POST'
	req.POST = {'pid': request.session['id'], 'status': 'Arrived'}
	request.session.pop('id')
	show_patients(req)

	return render(request, 'allset.html')