"""u

Revision ID: efd86b945e49
Revises: e0e881d0fbb1
Create Date: 2023-07-29 16:55:09.123226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'efd86b945e49'
down_revision = 'e0e881d0fbb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('birthdate', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('avatar', sa.String(), nullable=True))
    op.add_column('user', sa.Column('gender', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'gender')
    op.drop_column('user', 'avatar')
    op.drop_column('user', 'birthdate')
    # ### end Alembic commands ###
