from django.shortcuts import render, redirect

# Create your views here.

from .models import Peminjam
from .forms import PeminjamForm

def update(request,update_id):
	akun_update = Peminjam.objects.get(id=update_id)
	
	data = {
		'subs_id'		: akun_update.subs_id,
		'borrow_date'	: akun_update.borrow_date,
		'item_id'		: akun_update.item_id,
		'return_id'		: akun_update.return_id,
		'fee'			: akun_update.fee,
	}
	akun_form = PeminjamForm(request.POST or None, initial=data, instance=akun_update)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('borrowing:list')

	context = {
		"page_title":"Update akun",
		"akun_form":akun_form,
	}

	return render(request,'borrowing/create.html',context)


def delete(request,delete_id):
	Peminjam.objects.filter(id=delete_id).delete()
	return redirect('borrowing:list')

def create(request):
	akun_form = PeminjamForm(request.POST or None)

	if request.method == 'POST':
		if akun_form.is_valid():
			akun_form.save()

		return redirect('borrowing:list')

	context = {
		"page_title":"Tambah akun",
		"akun_form":akun_form,
	}

	return render(request,'borrowing/create.html',context)

def list(request):
	semua_akun = Peminjam.objects.all()

	context = {
		'page_title':'Borrowing',
		'semua_akun':semua_akun,
	}

	return render(request,'borrowing/list.html',context)