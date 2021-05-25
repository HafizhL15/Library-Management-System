from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from borrowing.models import Peminjam

def index(request):
    return render(request,'index.html')

def laporan(request):
	cursor=connection.cursor()
	cursor.execute("select borrowing_peminjam.subscriber_id, borrowing_peminjam.borrow_date, borrowing_peminjam.items_id, borrowing_peminjam.return_date, borrowing_peminjam.fee from borrowing_peminjam where DATEDIFF (borrowing_peminjam.return_date, borrowing_peminjam.borrow_date) > 21")
	result=cursor.fetchall()

	context = {
		'page_title' : 'Laporan Daftar Pinjaman yang sudah lewat waktu pengembalian',
		'daftars' : result,
	}

	return render(request,'laporan.html',context)
