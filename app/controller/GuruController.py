from app.model.guru import Guru
from app import response, app, db
from flask import request

def index():
    try:
        guru = Guru.query.all()
        data = formatarray(guru)
        return response.success(data, "success")
    except Exception as e:
        print(e)
        return response.error("Terjadi kesalahan saat mengambil data guru.")

def formatarray(datas):
    array = []
    for i in datas:
        array.append(singleObject(i))
    return array

def singleObject(data):
    data = {
        'id_guru': data.id_guru,
        'nama': data.nama,
        'nip': data.nip,
        'mata_pelajaran': data.mata_pelajaran,
        'no_telp': data.no_telp
    }
    return data