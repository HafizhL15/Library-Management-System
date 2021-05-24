from django import forms

from .models import Pelanggan

class PelangganForm(forms.ModelForm):
	class Meta:
		model = Pelanggan
		fields =[
			'tipe',
			'name',
			'address',
			'phone',
			'email',
		]