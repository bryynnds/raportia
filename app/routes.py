# routes.py
from flask import render_template
from app import app
from app.controller.BerandaController import show_beranda

@app.route('/')
def beranda():
    return show_beranda()

@app.route('/data_siswa')
def data_siswa():
    return render_template('data_siswa.html')

@app.route('/input')
def input():
    return render_template('input.html')

@app.route('/cetak')
def cetak():
    return render_template('cetak.html')

@app.route('/daftar_nilai')
def daftar_nilai():
    return render_template('daftar_nilai.html')

@app.route('/profil')
def profil():
    return render_template('profil.html')

@app.route('/login')
def login():
    return render_template('login.html')
