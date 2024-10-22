from flask import render_template
from app import db
from app.model.siswa import Siswa  # Model Siswa
from app.model.mataPelajaran import MataPelajaran  # Model MataPelajaran

def show_beranda():
    students = Siswa.query.all()
    mata_pelajaran_list = MataPelajaran.query.all()
    jumlah_mata_pelajaran = MataPelajaran.query.count()

    # Mengembalikan render template dengan semua data
    return render_template('beranda.html', 
                           students=students, 
                           mata_pelajaran=mata_pelajaran_list, 
                           jumlah_mata_pelajaran=jumlah_mata_pelajaran)