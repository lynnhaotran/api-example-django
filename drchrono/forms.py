from django import forms
from django.forms import extras

GENDER_CHOICES = (
	('Female', 'Female'),
	('Male', 'Male'),
	('Other', 'Other')
)

# forms go here
class PatientForm(forms.Form):
	first_name = forms.CharField(label="First name", max_length=100)
	last_name = forms.CharField(label="Last name", max_length=100)

class DemographicsForm(forms.Form):
	social_security_number = forms.CharField(label="Patient SSN", max_length=11, required=False)
	date_of_birth = forms.DateField(label="Date of Birth", required=False)
	gender = forms.ChoiceField(choices = GENDER_CHOICES, label="Gender")
	home_phone = forms.CharField(label="Home Phone Number", max_length=30, required=False)
	cell_phone = forms.CharField(label="Cell Phone Number", max_length=30, required=False)
	email = forms.CharField(label="E-mail", max_length=100, required=False)
	street_address = forms.CharField(label="Street Address", max_length=200, required=False)
	city = forms.CharField(label="City", max_length=100, required=False)
	state = forms.CharField(label="State", max_length=2, required=False)
	zip_code = forms.CharField(label="Zip Code", max_length=30, required=False)