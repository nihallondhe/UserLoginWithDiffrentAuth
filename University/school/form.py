from django.forms import ModelForm

from .models import Suggetions


class addsugestion(ModelForm):
	class Meta:
		model = Suggetions
		fields = '__all__'