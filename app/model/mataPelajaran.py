from app import db
from app.model.guru import Guru

class MataPelajaran(db.Model):
    id_mata_pelajaran = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_pelajaran = db.Column(db.String(100), nullable=False)
    id_guru = db.Column(db.BigInteger, db.ForeignKey(Guru.id_guru, ondelete='CASCADE'), nullable=False)

    def __repr__(self):
        return f'<MataPelajaran {self.nama_pelajaran} - {self.id_guru}>'
