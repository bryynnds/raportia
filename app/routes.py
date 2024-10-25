# routes.py
from flask import render_template
from app import app
from app.controller.BerandaController import show_beranda

@app.route('/')
def beranda():
    return show_beranda()

@app.route('/data_siswa')
def data_siswa():
    # Logika untuk menampilkan halaman Data Siswa
    return render_template('data_siswa.html')

@app.route('/input')
def input():
    # Logika untuk menampilkan halaman Input
    return render_template('input.html')

@app.route('/cetak')
def cetak():
    # Logika untuk menampilkan halaman Cetak
    return render_template('cetak.html')

@app.route('/daftar_nilai')
def daftar_nilai():
    # Logika untuk menampilkan halaman Daftar Nilai
    return render_template('daftar_nilai.html')
