"""empty message

Revision ID: 4303b334075b
Revises: 4aaff66a202b
Create Date: 2022-11-09 14:39:11.714402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4303b334075b'
down_revision = '4aaff66a202b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('username', sa.String(), nullable=True))
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.drop_column('user', 'first_name')
    op.drop_column('user', 'last_name')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.add_column('user', sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_column('user', 'username')
    # ### end Alembic commands ###
