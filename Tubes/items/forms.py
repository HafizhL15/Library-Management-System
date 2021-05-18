from django import forms

from .models import Barang

class BarangForm(forms.ModelForm):
	class Meta:
		model = Barang
		fields =[
			'librari',
			'category',
			'title',
			'author',
			'publisher',
			'year',
			'copies',
		]