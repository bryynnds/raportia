"""membuat table siswa

Revision ID: 051589f2f3bd
Revises: 167cc47fda0c
Create Date: 2024-10-22 01:10:00.979348

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '051589f2f3bd'
down_revision = '167cc47fda0c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('siswa',
    sa.Column('id_siswa', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('nisn', sa.String(length=20), nullable=False),
    sa.Column('nama', sa.String(length=100), nullable=False),
    sa.Column('tanggal_lahir', sa.Date(), nullable=False),
    sa.Column('jenis_kelamin', sa.Enum('L', 'P', name='jeniskelaminenum'), nullable=False),
    sa.Column('alamat', sa.Text(), nullable=False),
    sa.Column('id_kelas', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['id_kelas'], ['kelas.id_kelas'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_siswa')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('siswa')
    # ### end Alembic commands ###