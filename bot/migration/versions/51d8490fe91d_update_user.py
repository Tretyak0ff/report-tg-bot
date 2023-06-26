"""update User

Revision ID: 51d8490fe91d
Revises: d47da09e827c
Create Date: 2023-06-23 00:10:41.814389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '51d8490fe91d'
down_revision = 'd47da09e827c'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('work_mode', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'work_mode')
    # ### end Alembic commands ###
