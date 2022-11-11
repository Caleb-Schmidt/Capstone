"""empty message

Revision ID: 2697093934c6
Revises: c38d6ea3faad
Create Date: 2022-11-09 23:34:50.207903

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2697093934c6'
down_revision = 'c38d6ea3faad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.TEXT(),
               type_=sa.String(length=500),
               existing_nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('post', 'body',
               existing_type=sa.String(length=500),
               type_=sa.TEXT(),
               existing_nullable=True)
    # ### end Alembic commands ###
