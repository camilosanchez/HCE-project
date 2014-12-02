from django.db import models

from apps.packages.models import ExtraPackage


# actividades para los dias del evento
class EventActivity(models.Model):

	event_date = models.DateField(auto_now=False)
	place_name = models.CharField(max_length=100)
	time_from = models.TimeField(auto_now=False)
	time_to = models.TimeField(auto_now=False)
	description = models.TextField()
	transfer_rate = models.PositiveSmallIntegerField()

	def __unicode__(self):
		return "%s %s %s" % (self.place_name, self.event_date, self.time_from)


# Registrations for the activities that will have place on the event
class ActivityAssist(models.Model):
	going = models.BooleanField(default=None)
	people_going_number = models.PositiveSmallIntegerField()
	activity_registration = models.ForeignKey(EventActivity, blank=True, null=True)

	def __unicode__(self):
		return "%s %s" % (self.going, self.people_going_number)

	
	



# Registrations for the extra activities that will have place before or after the event
class ExtraRegistration(models.Model):

	extra_adult_name_1 = models.CharField(max_length=50)
	extra_adult_passport_1 = models.PositiveIntegerField()

	extra_adult_name_2 = models.CharField(max_length=50)
	extra_adult_passport_2 = models.PositiveIntegerField()

	extra_adult_name_3 = models.CharField(max_length=50)
	extra_adult_passport_3 = models.PositiveIntegerField()

	extra_adult_name_4 = models.CharField(max_length=50)
	extra_adult_passport_4 = models.PositiveIntegerField()

	extra_adult_name_5 = models.CharField(max_length=50)
	extra_adult_passport_5 = models.PositiveIntegerField()

	extra_adult_name_6 = models.CharField(max_length=50)
	extra_adult_passport_6 = models.PositiveIntegerField()

	extra_child_name_1 = models.CharField(max_length=50)
	extra_child_passport_1 = models.PositiveIntegerField()
	extra_child_age_1 = models.PositiveSmallIntegerField()

	extra_child_name_2 = models.CharField(max_length=50)
	extra_child_passport_2 = models.PositiveIntegerField()
	extra_child_age_2 = models.PositiveSmallIntegerField()

	extra_child_name_3 = models.CharField(max_length=50)
	extra_child_passport_3 = models.PositiveIntegerField()
	extra_child_age_3 = models.PositiveSmallIntegerField()

	extra_child_name_4 = models.CharField(max_length=50)
	extra_child_passport_4 = models.PositiveIntegerField()
	extra_child_age_4 = models.PositiveSmallIntegerField()

	extra_child_name_5 = models.CharField(max_length=50)
	extra_child_passport_5 = models.PositiveIntegerField()
	extra_child_age_5 = models.PositiveSmallIntegerField()

	extra_child_name_6 = models.CharField(max_length=50)
	extra_child_passport_6 = models.PositiveIntegerField()
	extra_child_age_6 = models.PositiveSmallIntegerField()

	reserve_before_event = models.BooleanField(default=None)
	reserve_after_event = models.BooleanField(default=None)
	checkin_date = models.DateField(auto_now=False)
	checkout_date = models.DateField(auto_now=False)

	def __unicode__(self):
		return "%s %s %s" % (self.extra_adult_name, self.checkin_date, self.checkout_date)


# actividades para antes o despues del evento
class ExtraActivity(models.Model):

	place_name = models.CharField(max_length=100)
	venue_location = models.CharField(max_length=100)
	price_from = models.PositiveSmallIntegerField()
	description = models.TextField()
	place_img = models.ImageField(upload_to='extra_activities')
	extra_package = models.ForeignKey(ExtraPackage)
	extra_registration = models.ForeignKey(ExtraRegistration, blank=True, null=True)

	def __unicode__(self):
		return self.place_name


class Interest(models.Model):

	interest_title = models.CharField(max_length=50)

	def __unicode__(self):
		return self.interest_title


# actividades para antes o despues del evento a la medida
class ExtraCustom(models.Model):		

	budget_from = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	budget_to = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)
	interests = models.TextField()
	options =  models.ManyToManyField(Interest)

	custom_adult_name_1 = models.CharField(max_length=50)
	custom_adult_passport_1 = models.PositiveIntegerField()

	custom_adult_name_2 = models.CharField(max_length=50)
	custom_adult_passport_2 = models.PositiveIntegerField()

	custom_adult_name_3 = models.CharField(max_length=50)
	custom_adult_passport_3 = models.PositiveIntegerField()

	custom_adult_name_4 = models.CharField(max_length=50)
	custom_adult_passport_4 = models.PositiveIntegerField()

	custom_adult_name_5 = models.CharField(max_length=50)
	custom_adult_passport_5 = models.PositiveIntegerField()

	custom_adult_name_6 = models.CharField(max_length=50)
	custom_adult_passport_6 = models.PositiveIntegerField()

	custom_child_name_1 = models.CharField(max_length=50)
	custom_child_passport_1 = models.PositiveIntegerField()
	custom_child_age_1 = models.PositiveSmallIntegerField()

	custom_child_name_2 = models.CharField(max_length=50)
	custom_child_passport_2 = models.PositiveIntegerField()
	custom_child_age_2 = models.PositiveSmallIntegerField()

	custom_child_name_3 = models.CharField(max_length=50)
	custom_child_passport_3 = models.PositiveIntegerField()
	custom_child_age_3 = models.PositiveSmallIntegerField()

	custom_child_name_4 = models.CharField(max_length=50)
	custom_child_passport_4 = models.PositiveIntegerField()
	custom_child_age_4 = models.PositiveSmallIntegerField()

	custom_child_name_5 = models.CharField(max_length=50)
	custom_child_passport_5 = models.PositiveIntegerField()
	custom_child_age_5 = models.PositiveSmallIntegerField()

	custom_child_name_6 = models.CharField(max_length=50)
	custom_child_passport_6 = models.PositiveIntegerField()
	custom_child_age_6 = models.PositiveSmallIntegerField()


	reserve_before_event = models.BooleanField(default=None)
	reserve_after_event = models.BooleanField(default=None)
	checkin_date = models.DateField(auto_now=False)
	checkout_date = models.DateField(auto_now=False)

	def __unicode__(self):
		return self.extra_adult_name

