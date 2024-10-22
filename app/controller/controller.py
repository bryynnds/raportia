from app.model.siswa import Siswa
from app.model.mataPelajaran import MataPelajaran
from app.model.nilai import Nilai

def get_siswa_with_mata_pelajaran():
    siswa_list = Siswa.query.all()
    return siswa_list

def get_mata_pelajaran():
    return MataPelajaran.query.all()

def get_nilai_for_siswa(siswa_id):
    return Nilai.query.filter_by(id_siswa=siswa_id).all()