from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import datetime, time, requests
from django.shortcuts import render
from settings import CLIENT_ID, CLIENT_SECRET_ID
from .models import Doctor

headers = {
	'Authorization' : Doctor.objects.get(username='lynnhaotran').access_token,
}

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

	# Save these in your database associated with the user
	# FIX: Missing timestamp - issue w pytz
	access_token = data['access_token']
	refresh_token = data['refresh_token']

	user_response = requests.get('https://drchrono.com/api/users/current', headers={
    'Authorization': 'Bearer %s' % access_token,
	})
	user_response.raise_for_status()
	user_data = user_response.json()

	# You can store this in your database along with the tokens
	username = user_data['username']

	user, created = Doctor.objects.get_or_create(username=username)
	user.access_token = access_token
	user.refresh_token = refresh_token
	user.save()

	return HttpResponseRedirect(reverse('landing'))

def landing(request):
	doctor = Doctor.objects.get(username='lynnhaotran')
	context = { 'doctor' : doctor }
	return render(request, 'landing.html')

def dashboard(request):
	access_token = Doctor.objects.get(username='lynnhaotran').access_token
	cur_date = str(datetime.date.today())
	response = requests.get('https://drchrono.com/api/appointments?date=' + cur_date, 
							headers={'Authorization': 'Bearer %s' % access_token,}).json()

	results = response['results']


	appointments = []
	for result in results:
		struct_time = datetime.datetime.strptime(result['scheduled_time'], '%Y-%m-%dT%H:%M:%S')

		#Get patient name
		patient = requests.get('https://drchrono.com/api/patients/' + str(result['patient']), 
							headers={'Authorization': 'Bearer %s' % access_token,}).json()

		appointment = { 
			'name' : patient['first_name'] + " " + patient['last_name'],
			'scheduled_time' : struct_time.time(),
			'duration' : result['duration'],
			'status' : result['status']
		}
		appointments.append(appointment)

	context = { 'appointments' : appointments}

	return render(request, 'dashboard.html', context)

