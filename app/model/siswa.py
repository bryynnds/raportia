from app import db
from app.model.kelas import Kelas
import enum

class JenisKelaminEnum(enum.Enum):
    L = 'Laki-laki'
    P = 'Perempuan'

class Siswa(db.Model):
    id_siswa = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    nisn = db.Column(db.String(20), nullable=False)
    nama = db.Column(db.String(100), nullable=False)
    tanggal_lahir = db.Column(db.Date, nullable=False)
    jenis_kelamin = db.Column(db.Enum(JenisKelaminEnum), nullable=False)
    alamat = db.Column(db.Text, nullable=False)
    id_kelas = db.Column(db.BigInteger, db.ForeignKey(Kelas.id_kelas, ondelete='CASCADE'))

    def __repr__(self):
        return f'<Siswa {self.nama}>'
