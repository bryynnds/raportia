from app import db

class Kelas(db.Model):
    id_kelas = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nama_kelas = db.Column(db.String(50), nullable=False)
    tahun_ajaran = db.Column(db.String(10), nullable=False)

    def __repr__(self):
        return f'<Kelas {self.nama_kelas}>'
