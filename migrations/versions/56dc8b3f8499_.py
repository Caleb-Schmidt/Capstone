"""empty message

Revision ID: 56dc8b3f8499
Revises: 2697093934c6
Create Date: 2022-11-20 20:07:59.852408

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '56dc8b3f8499'
down_revision = '2697093934c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('is_admin', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'is_admin')
    # ### end Alembic commands ###
