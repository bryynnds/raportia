from app import db
from app.model.siswa import Siswa
from app.model.kelas import Kelas

class Laporan(db.Model):
    id_laporan = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_siswa = db.Column(db.BigInteger, db.ForeignKey(Siswa.id_siswa, ondelete='CASCADE'), nullable=False)
    id_kelas = db.Column(db.BigInteger, db.ForeignKey(Kelas.id_kelas, ondelete='CASCADE'), nullable=False)
    deskripsi = db.Column(db.Text, nullable=False)
    tanggal = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'<Laporan Siswa {self.id_siswa} - Kelas {self.id_kelas}>'
