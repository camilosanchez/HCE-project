from django.db import models

class PackageData(models.Model):

	text = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

	class Meta:
		abstract = True


class HotelPackage(PackageData):
	
	def __unicode__(self):
		return self.text

class ExtraPackage(PackageData):
	
	def __unicode__(self):
		return self.text

class TransferPackage(PackageData):

	def __unicode__(self):
		return self.text