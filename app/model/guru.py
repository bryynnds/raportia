from app import db

class Guru(db.Model):
    id_guru = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama = db.Column(db.String(100), nullable=False)
    nip = db.Column(db.String(20), nullable=False)
    mata_pelajaran = db.Column(db.String(50), nullable=False)
    no_telp = db.Column(db.String(13), nullable=False)

    def __repr__(self):
        return f'<Guru {self.nama}>'
