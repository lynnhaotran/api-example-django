import requests, datetime, time, pytz
from .models import Patient

def API_request(url, access_token):
	response = requests.get(url, headers={
    'Authorization': 'Bearer %s' % access_token,
	})
	response.raise_for_status()

	return response.json()

def create_patient_database(request, utc_time, tz):

	cur_date = pytz.utc.localize(utc_time, is_dst=None).astimezone(tz).replace(tzinfo=None)

	appointment_data = API_request('https://drchrono.com/api/appointments?date=' + str(cur_date), 
									request.session['access_token'])
	appointments = appointment_data['results']

	for appointment in appointments:
		scheduled_time = datetime.datetime.strptime(appointment['scheduled_time'], '%Y-%m-%dT%H:%M:%S')
		start_time = scheduled_time.strftime("%H:%M")
		
		#Get patient information
		patient = API_request('https://drchrono.com/api/patients/' + str(appointment['patient']), 
								request.session['access_token'])
		
		Patient.objects.create(pid=appointment['patient'], first_name=patient['first_name'], last_name=patient['last_name'], 
									scheduled_time=scheduled_time, start_time=start_time, duration=appointment['duration'], status=appointment['status'])

'''def update_wait_time(tz):

	arrived_patients = Patient.objects.filter(status="Arrived")
	
	for patient in arrived_patients:
		time_diff = datetime.datetime.now() - patient.checkin_time.astimezone(tz).replace(tzinfo=None)
		patient.wait_time = time_diff.seconds / 60
		patient.save()'''