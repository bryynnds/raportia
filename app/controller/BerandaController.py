# BerandaController.py
from flask import render_template
from app import db
from app.model.siswa import Siswa  # Model Siswa
from app.model.nilai import Nilai  # Model Nilai

def show_beranda():
    # Mengambil semua data siswa dari database
    siswa_list = Siswa.query.all()
    
    # Kirim data siswa ke template
    return render_template('index.html', siswa_list=siswa_list)

def show_data_siswa():
    # Mengambil semua data siswa dari database
    siswa_list = Siswa.query.all()
    
    # Kirim data siswa ke template
    return render_template('data_siswa.html', siswa_list=siswa_list)