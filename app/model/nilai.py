from app import db
from app.model.siswa import Siswa
from app.model.mataPelajaran import MataPelajaran

class Nilai(db.Model):
    id_nilai = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_siswa = db.Column(db.BigInteger, db.ForeignKey(Siswa.id_siswa, ondelete='CASCADE'), nullable=False)
    id_mata_pelajaran = db.Column(db.BigInteger, db.ForeignKey(MataPelajaran.id_mata_pelajaran, ondelete='CASCADE'), nullable=False)
    nilai_tugas = db.Column(db.Numeric(10, 0), nullable=False)
    nilai_uts = db.Column(db.Numeric(10, 0), nullable=False)
    nilai_uas = db.Column(db.Numeric(10, 0), nullable=False)
    nilai_akhr = db.Column(db.Numeric(10, 0), nullable=False)

    def __repr__(self):
        return f'<Nilai Siswa {self.id_siswa} - Mata Pelajaran {self.id_mata_pelajaran}>'
