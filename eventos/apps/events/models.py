from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

from phonenumber_field.modelfields import PhoneNumberField

from apps.activities.models import EventActivity, ExtraActivity, ExtraCustom
from apps.packages.models import TransferPackage, HotelPackage


class TimeStampModel(models.Model):

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	class Meta:
		abstract = True


# General registration model
class Registration(TimeStampModel):

	GENDER_CHOICES = (
		('S', 'Cual es su sexo?'),
		('M', 'Hombre'),
		('F', 'Mujer'),
	)
	
	book_first_name = models.CharField(max_length=50)
	book_last_name = models.CharField(max_length=50)
	book_phone = PhoneNumberField()
	book_email = models.EmailField()
	book_passport = models.PositiveIntegerField()
	book_nationality = models.CharField(max_length=100)
	book_sex = models.CharField(max_length=1, choices =GENDER_CHOICES)
	book_special_requirements = models.TextField()

	city_of_flight_origin = models.CharField(max_length=100)
	arrival_date = models.DateField(auto_now=False)
	leaving_date = models.DateField(auto_now=False)

	traveling_adult_name_1 = models.CharField(max_length=100)
	traveling_adult_passport_1 = models.PositiveIntegerField()
	traveling_adult_email_1 = models.EmailField()

	traveling_adult_name_2 = models.CharField(max_length=100)
	traveling_adult_passport_2 = models.PositiveIntegerField()
	traveling_adult_email_2 = models.EmailField()

	traveling_adult_name_3 = models.CharField(max_length=100)
	traveling_adult_passport_3 = models.PositiveIntegerField()
	traveling_adult_email_3 = models.EmailField()

	traveling_adult_name_4 = models.CharField(max_length=100)
	traveling_adult_passport_4 = models.PositiveIntegerField()
	traveling_adult_email_4 = models.EmailField()

	traveling_adult_name_5 = models.CharField(max_length=100)
	traveling_adult_passport_5 = models.PositiveIntegerField()
	traveling_adult_email_5 = models.EmailField()

	traveling_adult_name_6 = models.CharField(max_length=100)
	traveling_adult_passport_6 = models.PositiveIntegerField()
	traveling_adult_email_6 = models.EmailField()


	traveling_child_name_1 = models.CharField(max_length=100)
	traveling_child_passport_1 = models.PositiveIntegerField()
	traveling_child_age_1 = models.PositiveSmallIntegerField()

	traveling_child_name_2 = models.CharField(max_length=100)
	traveling_child_passport_2 = models.PositiveIntegerField()
	traveling_child_age_2 = models.PositiveSmallIntegerField()

	traveling_child_name_3 = models.CharField(max_length=100)
	traveling_child_passport_3 = models.PositiveIntegerField()
	traveling_child_age_3 = models.PositiveSmallIntegerField()

	traveling_child_name_4 = models.CharField(max_length=100)
	traveling_child_passport_4 = models.PositiveIntegerField()
	traveling_child_age_4 = models.PositiveSmallIntegerField()

	traveling_child_name_5 = models.CharField(max_length=100)
	traveling_child_passport_5 = models.PositiveIntegerField()
	traveling_child_age_5 = models.PositiveSmallIntegerField()

	traveling_child_name_6 = models.CharField(max_length=100)
	traveling_child_passport_6 = models.PositiveIntegerField()
	traveling_child_age_6 = models.PositiveSmallIntegerField()


	airport_transfer = models.ForeignKey(TransferPackage, blank=True, null=True)

	hotel_checkin_date = models.DateField(auto_now=False)
	hotel_checkout_date = models.DateField(auto_now=False)
	hotel_package = models.ForeignKey(HotelPackage, blank= True, null=True)

	hotel_room_adult_name_1 = models.CharField(max_length=100)
	hotel_room_adult_passport_1 = models.PositiveIntegerField()
	hotel_room_adult_email_1 = models.EmailField()

	hotel_room_adult_name_2 = models.CharField(max_length=100)
	hotel_room_adult_passport_2 = models.PositiveIntegerField()
	hotel_room_adult_email_2 = models.EmailField()

	hotel_room_adult_name_3 = models.CharField(max_length=100)
	hotel_room_adult_passport_3 = models.PositiveIntegerField()
	hotel_room_adult_email_3 = models.EmailField()

	hotel_room_adult_name_4 = models.CharField(max_length=100)
	hotel_room_adult_passport_4 = models.PositiveIntegerField()
	hotel_room_adult_email_4 = models.EmailField()

	hotel_room_adult_name_5 = models.CharField(max_length=100)
	hotel_room_adult_passport_5 = models.PositiveIntegerField()
	hotel_room_adult_email_5 = models.EmailField()

	hotel_room_adult_name_6 = models.CharField(max_length=100)
	hotel_room_adult_passport_6 = models.PositiveIntegerField()
	hotel_room_adult_email_6 = models.EmailField()

	hotel_room_child_name_1 = models.CharField(max_length=50)
	hotel_room_child_passport_1 = models.PositiveIntegerField()
	hotel_room_child_age_1 = models.PositiveSmallIntegerField()

	hotel_room_child_name_2 = models.CharField(max_length=50)
	hotel_room_child_passport_2 = models.PositiveIntegerField()
	hotel_room_child_age_2 = models.PositiveSmallIntegerField()

	hotel_room_child_name_3 = models.CharField(max_length=50)
	hotel_room_child_passport_3 = models.PositiveIntegerField()
	hotel_room_child_age_3 = models.PositiveSmallIntegerField()

	hotel_room_child_name_4 = models.CharField(max_length=50)
	hotel_room_child_passport_4 = models.PositiveIntegerField()
	hotel_room_child_age_4 = models.PositiveSmallIntegerField()

	hotel_room_child_name_5 = models.CharField(max_length=50)
	hotel_room_child_passport_5 = models.PositiveIntegerField()
	hotel_room_child_age_5 = models.PositiveSmallIntegerField()

	hotel_room_child_name_6 = models.CharField(max_length=50)
	hotel_room_child_passport_6 = models.PositiveIntegerField()
	hotel_room_child_age_6 = models.PositiveSmallIntegerField()

	cc_number = models.PositiveIntegerField()
	exp_date = models.DateField(auto_now=False)
	cvv_number = models.PositiveSmallIntegerField()
	cc_address = models.CharField(max_length=50)

	event_activities = models.ManyToManyField(EventActivity, blank=True, null=True)

	extra_activities = models.ForeignKey(ExtraActivity, blank=True, null=True)

	extra_activities_custom = models.OneToOneField(ExtraCustom, blank=True, null=True)

	def __unicode__(self):
		return "%s %s" % (self.book_first_name , self.book_last_name)


class Event(TimeStampModel):
	
	event_name = models.CharField(max_length=50)
	event_initial_date = models.DateField(auto_now=False)
	event_ending_date = models.DateField(auto_now=False)
	organizer = models.ForeignKey(User)
	event_slug = models.SlugField(editable=False)
	description = models.TextField()
	hotel_name = models.CharField(max_length=100)
	hotel_address = models.CharField(max_length=100)
	registrations = models.ForeignKey(Registration, blank=True, null=True)


	def save(self, *args, **kwargs):
		if not self.id:
			self.slug = slugify(self.event_name)
		super(Event, self).save(*args, **kwargs)

	def __unicode__(self):
		return "%s %s" (self.event_name, self.event_initial_date, self.event_ending_date)