"""field_pr

Revision ID: 0b16d7bd43d1
Revises: e89082d8cb86
Create Date: 2023-07-29 09:15:22.415172

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0b16d7bd43d1'
down_revision = 'e89082d8cb86'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('field', sa.Column('price', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('field', 'price')
    # ### end Alembic commands ###
