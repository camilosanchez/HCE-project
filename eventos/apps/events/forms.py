#encoding: utf-8
from django import forms
from .models import Registration
from apps.activities.models import ActivityAssist, ExtraActivity, ExtraRegistration, ExtraCustom


class FormStep1(forms.ModelForm):
	class Meta:
		model = Registration
		fields = ['book_first_name', 'book_last_name', 'book_phone', 'book_email', 'book_passport', 
					'book_nationality', 'book_sex', 'book_special_requirements']
		widgets = {
			'book_first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su nombre'}),
			'book_last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su apellido'}),
			'book_phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej.: 809-562-3000'}),
			'book_email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ej.: juan@travelwise.com.do'}),
			'book_passport': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Escriba su número de pasaporte'}),
			'book_nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nacionalidad', 'id': 'typeahead-demo-01'}),
			'book_sex': forms.Select(attrs={'class': 'form-control select select-primary select-lg', 'data-toggle':'select',}),
			'book_special_requirements': forms.Textarea(attrs={'class': 'form-control', 'rows': '2',
				'placeholder': 'Ejemplo: Alergias, Restricciones de dieta, condiciones físicas o de salud (sillas de rueda) etc.',
				}),
		}


class FormStep2(forms.ModelForm):
	traveling_adult_name_1 = forms.CharField()
	traveling_adult_passport_1 = forms.CharField()
	traveling_adult_email_1 = forms.CharField()
	traveling_adult_name_2 = forms.CharField(required=False)
	traveling_adult_passport_2 = forms.CharField(required=False)
	traveling_adult_email_2 = forms.CharField(required=False)
	traveling_adult_name_3 = forms.CharField(required=False)
	traveling_adult_passport_3 = forms.CharField(required=False)
	traveling_adult_email_3 = forms.CharField(required=False)
	traveling_adult_name_4 = forms.CharField(required=False)
	traveling_adult_passport_4 = forms.CharField(required=False)
	traveling_adult_email_4 = forms.CharField(required=False)
	traveling_adult_name_5 = forms.CharField(required=False)
	traveling_adult_passport_5 = forms.CharField(required=False)
	traveling_adult_email_5 = forms.CharField(required=False)
	traveling_adult_name_6 = forms.CharField(required=False)
	traveling_adult_passport_6 = forms.CharField(required=False)
	traveling_adult_email_6 = forms.CharField(required=False)
	traveling_child_name_1 = forms.CharField(required=False)
	traveling_child_passport_1 = forms.CharField(required=False)
	traveling_child_age_1 = forms.CharField(required=False)
	traveling_child_name_2 = forms.CharField(required=False)
	traveling_child_passport_2 = forms.CharField(required=False)
	traveling_child_age_2 = forms.CharField(required=False)
	traveling_child_name_3 = forms.CharField(required=False)
	traveling_child_passport_3 = forms.CharField(required=False)
	traveling_child_age_3 = forms.CharField(required=False)
	traveling_child_name_4 = forms.CharField(required=False)
	traveling_child_passport_4 = forms.CharField(required=False)
	traveling_child_age_4 = forms.CharField(required=False)
	traveling_child_name_5 = forms.CharField(required=False)
	traveling_child_passport_5 = forms.CharField(required=False)
	traveling_child_age_5 = forms.CharField(required=False)
	traveling_child_name_6 = forms.CharField(required=False)
	traveling_child_passport_6 = forms.CharField(required=False)
	traveling_child_age_6 = forms.CharField(required=False)

	class Meta:
		model = Registration
		fields = ['city_of_flight_origin', 'arrival_date', 'leaving_date', 
					'traveling_adult_name_1',
					'traveling_adult_passport_1',
					'traveling_adult_email_1',
					'traveling_adult_name_2',
					'traveling_adult_passport_2',
					'traveling_adult_email_2',
					'traveling_adult_name_3',
					'traveling_adult_passport_3',
					'traveling_adult_email_3',
					'traveling_adult_name_4',
					'traveling_adult_passport_4',
					'traveling_adult_email_4',
					'traveling_adult_name_5',
					'traveling_adult_passport_5',
					'traveling_adult_email_5',
					'traveling_adult_name_6',
					'traveling_adult_passport_6',
					'traveling_adult_email_6',
					'traveling_child_name_1',
					'traveling_child_passport_1',
					'traveling_child_age_1',
					'traveling_child_name_2',
					'traveling_child_passport_2',
					'traveling_child_age_2',
					'traveling_child_name_3',
					'traveling_child_passport_3',
					'traveling_child_age_3',
					'traveling_child_name_4',
					'traveling_child_passport_4',
					'traveling_child_age_4',
					'traveling_child_name_5',
					'traveling_child_passport_5',
					'traveling_child_age_5',
					'traveling_child_name_6',
					'traveling_child_passport_6',
					'traveling_child_age_6',
					]
		widgets = {
			'city_of_flight_origin': forms.TextInput(attrs={'class': ''}),
			'arrival_date': forms.TextInput(attrs={'class': ''}),
			'leaving_date': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_1': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_1': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_1': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_2': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_2': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_2': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_3': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_3': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_3': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_4': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_4': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_4': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_5': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_5': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_5': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_name_6': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_passport_6': forms.TextInput(attrs={'class': ''}),
			'traveling_adult_email_6': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_1': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_1': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_1': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_2': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_2': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_2': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_3': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_3': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_3': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_4': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_4': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_4': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_5': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_5': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_5': forms.TextInput(attrs={'class': ''}),
			'traveling_child_name_6': forms.TextInput(attrs={'class': ''}),
			'traveling_child_passport_6': forms.TextInput(attrs={'class': ''}),
			'traveling_child_age_6': forms.TextInput(attrs={'class': ''}),
			'airport_transfer': forms.Select(attrs={'class': ''})	
		}

class FormStep3(forms.ModelForm):

	hotel_room_adult_name_1 = forms.CharField()
	hotel_room_adult_passport_1 = forms.CharField()
	hotel_room_adult_email_1 = forms.CharField()
	hotel_room_adult_name_2 = forms.CharField(required=False)
	hotel_room_adult_passport_2 = forms.CharField(required=False)
	hotel_room_adult_email_2 = forms.CharField(required=False)
	hotel_room_adult_name_3 = forms.CharField(required=False)
	hotel_room_adult_passport_3 = forms.CharField(required=False)
	hotel_room_adult_email_3 = forms.CharField(required=False)
	hotel_room_adult_name_4 = forms.CharField(required=False)
	hotel_room_adult_passport_4 = forms.CharField(required=False)
	hotel_room_adult_email_4 = forms.CharField(required=False)
	hotel_room_adult_name_5 = forms.CharField(required=False)
	hotel_room_adult_passport_5 = forms.CharField(required=False)
	hotel_room_adult_email_5 = forms.CharField(required=False)
	hotel_room_adult_name_6 = forms.CharField(required=False)
	hotel_room_adult_passport_6 = forms.CharField(required=False)
	hotel_room_adult_email_6 = forms.CharField(required=False)
	hotel_room_child_name_1 = forms.CharField(required=False)
	hotel_room_child_passport_1 = forms.CharField(required=False)
	hotel_room_child_age_1 = forms.CharField(required=False)
	hotel_room_child_name_2 = forms.CharField(required=False)
	hotel_room_child_passport_2 = forms.CharField(required=False)
	hotel_room_child_age_2 = forms.CharField(required=False)
	hotel_room_child_name_3 = forms.CharField(required=False)
	hotel_room_child_passport_3 = forms.CharField(required=False)
	hotel_room_child_age_3 = forms.CharField(required=False)
	hotel_room_child_name_4 = forms.CharField(required=False)
	hotel_room_child_passport_4 = forms.CharField(required=False)
	hotel_room_child_age_4 = forms.CharField(required=False)
	hotel_room_child_name_5 = forms.CharField(required=False)
	hotel_room_child_passport_5 = forms.CharField(required=False)
	hotel_room_child_age_5 = forms.CharField(required=False)
	hotel_room_child_name_6 = forms.CharField(required=False)
	hotel_room_child_passport_6 = forms.CharField(required=False)
	hotel_room_child_age_6 = forms.CharField(required=False)
	class Meta:
		model = Registration
		fields = [	
		'hotel_checkin_date', 'hotel_checkout_date','hotel_package',
		'hotel_room_adult_name_1',
		'hotel_room_adult_passport_1',
		'hotel_room_adult_email_1',
		'hotel_room_adult_name_2',
		'hotel_room_adult_passport_2',
		'hotel_room_adult_email_2',
		'hotel_room_adult_name_3',
		'hotel_room_adult_passport_3',
		'hotel_room_adult_email_3',
		'hotel_room_adult_name_4',
		'hotel_room_adult_passport_4',
		'hotel_room_adult_email_4',
		'hotel_room_adult_name_5',
		'hotel_room_adult_passport_5',
		'hotel_room_adult_email_5',
		'hotel_room_adult_name_6',
		'hotel_room_adult_passport_6',
		'hotel_room_adult_email_6',
		'hotel_room_child_name_1',
		'hotel_room_child_passport_1',
		'hotel_room_child_age_1',
		'hotel_room_child_name_2',
		'hotel_room_child_passport_2',
		'hotel_room_child_age_2',
		'hotel_room_child_name_3',
		'hotel_room_child_passport_3',
		'hotel_room_child_age_3',
		'hotel_room_child_name_4',
		'hotel_room_child_passport_4',
		'hotel_room_child_age_4',
		'hotel_room_child_name_5',
		'hotel_room_child_passport_5',
		'hotel_room_child_age_5',
		'hotel_room_child_name_6',
		'hotel_room_child_passport_6',
		'hotel_room_child_age_6',

		'cc_number',
		'exp_date',
		'cvv_number',
		'cc_address',]


class FormStep4(forms.ModelForm):
	class Meta:
		model = ActivityAssist
		fields = ['going', 'people_going_number', 'activity_registration']
		widgets = {
			}


class FormStep5(forms.ModelForm):
	class Meta:
		model = ExtraActivity
		confirm = forms.BooleanField()
		exclude = ['place_img']
		# fields = ['confirm']

class DetalleHotel(forms.ModelForm):
	class Meta:
		model = ExtraRegistration
		confirm = forms.BooleanField()

class DetalleCustom(forms.ModelForm):
	class Meta:
		model = ExtraCustom
		confirm = forms.BooleanField()



class FormStep6(forms.Form):
	confirm = forms.BooleanField()


