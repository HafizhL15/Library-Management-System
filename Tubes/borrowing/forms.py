from django import forms

from .models import Peminjam

class PeminjamForm(forms.ModelForm):
	class Meta:
		model = Peminjam
		fields =[
			'subs_id',
			'borrow_date',
			'item_id',
			'return_date',
			'fee',
		]