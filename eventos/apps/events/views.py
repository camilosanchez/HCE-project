from django.shortcuts import render
from django.contrib.formtools.wizard.views import SessionWizardView
from django.forms.models import model_to_dict

from .forms import FormStep1, FormStep2, FormStep3, FormStep4, FormStep5, FormStep6, DetalleHotel, DetalleCustom
from .models import Registration
from apps.activities.models import EventActivity, ActivityAssist

FORMS = [
	("step1", FormStep1),
	("step2", FormStep2),
	("step3", FormStep3),
	("step4", FormStep4),
	("step5", FormStep5),
	("step6", FormStep6),
	("detalle_hotel", DetalleHotel),
	("detalle_custom", DetalleCustom)
]

TEMPLATES = {
	"step1" : "wizard/step1.html",
	"step2" : "wizard/step2.html",
	"step3" : "wizard/step3.html",
	"step4" : "wizard/step4.html",
	"step5" : "wizard/step5.html",
	"step6" : "wizard/step6.html",
	"detalle_hotel" : "wizard/detalle_hotel.html",
	"detalle_custom" : "wizard/detalle_custom.html"
}

class RegisterStepsWizard(SessionWizardView):

	
	instance = None

	def get_context_data(self, form, **kwargs):
		context = super(RegisterStepsWizard, self).get_context_data(form=form, **kwargs)

		if self.steps.current == 'step4':
			activity_object = EventActivity.objects.all()
			if self.request.method == "POST":
				activity_object_count = activity_object.count()
				assistant_form = [FormStep4(self.request.POST, prefix=str(x), instance=ActivityAssist()) for x in range(0, activity_object_count)]
				context ['actividades_forms'] = zip (assistant_form, activity_object)
			else:
				activity_object_count = activity_object.count()
				assistant_form = [FormStep4(self.request.POST, prefix=str(x), instance=ActivityAssist()) for x in range(0, activity_object_count)]
				context ['actividades_forms'] = zip (assistant_form, activity_object)
			
		print context['wizard']
		print self.steps.__class__
		print self.get_form
		# import pdb; pdb.set_trace()
		return context

	def get_template_names(self):
		return [TEMPLATES[self.steps.current]]

	def get_form_instance(self, step):
		if self.instance is None:
			self.instance = Registration()
		return self.instance 

	def done(self, form_list, **kwargs):
		self.instance.save()


		return HttpResponseRedirect('/wizard/confirmacion.html/')