"""update model nilai

Revision ID: b05db22d6acd
Revises: ff77cec90644
Create Date: 2024-11-02 19:49:26.395838

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b05db22d6acd'
down_revision = 'ff77cec90644'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('nilai',
    sa.Column('id_nilai', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('id_siswa', sa.BigInteger(), nullable=False),
    sa.Column('id_mata_pelajaran', sa.BigInteger(), nullable=False),
    sa.Column('nilai_akhir', sa.Numeric(precision=10, scale=0), nullable=False),
    sa.ForeignKeyConstraint(['id_mata_pelajaran'], ['mata_pelajaran.id_mata_pelajaran'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['id_siswa'], ['siswa.id_siswa'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id_nilai')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('nilai')
    # ### end Alembic commands ###
