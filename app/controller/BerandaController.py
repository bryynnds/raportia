from flask import render_template
from app import db
from app.model.siswa import Siswa  # Model Siswa

def show_beranda():
    # Mengambil semua data siswa dari database
    siswa_list = Siswa.query.all()
    
    # Kirim data siswa ke template
    return render_template('index.html', siswa_list=siswa_list)
