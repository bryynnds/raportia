from app import app, db
from flask import request, redirect, url_for, render_template
from app.controller import GuruController
from app.controller.BerandaController import show_beranda

from app.controller.controller import get_siswa_with_mata_pelajaran, get_mata_pelajaran, get_nilai_for_siswa

@app.route('/guru', methods=['GET', 'POST'])
def gurus():
  if request.method=='GET':
    return GuruController.index()
  else:
    return GuruController.save()
  
  return 'Guru'

@app.route('/')
def beranda():
    return show_beranda()
  
@app.route('/admin/<name>')
def admin(name):
    return render_template("index.html", content=name)

@app.route('/success/<name>')
def success(name):
    return 'walcome %s' % name
