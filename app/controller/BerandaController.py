from flask import render_template
from app import db
from app.model.siswa import Siswa  # Model Siswa
from app.model.mataPelajaran import MataPelajaran  # Model MataPelajaran

def show_beranda():

    return render_template('index.html')