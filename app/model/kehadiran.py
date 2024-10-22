from app import db
from app.model.siswa import Siswa
import enum

class StatusKehadiranEnum(enum.Enum):
    Hadir = 'Hadir'
    Sakit = 'Sakit'
    Alpa = 'Alpa'

class Kehadiran(db.Model):
    id_kehadiran = db.Column(db.BigInteger, primary_key=True, autoincrement=True)
    id_siswa = db.Column(db.BigInteger, db.ForeignKey(Siswa.id_siswa, ondelete='CASCADE'))
    tanggal = db.Column(db.Date, nullable=False)
    status = db.Column(db.Enum(StatusKehadiranEnum), nullable=False)

    def __repr__(self):
        return f'<Kehadiran {self.id_siswa} - {self.tanggal}>'
