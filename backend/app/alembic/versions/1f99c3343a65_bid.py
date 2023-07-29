"""bid

Revision ID: 1f99c3343a65
Revises: a96363ac87a9
Create Date: 2023-07-29 11:44:33.254746

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f99c3343a65'
down_revision = 'a96363ac87a9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bid', sa.Column('actual_amount', sa.Integer(), nullable=True))
    op.drop_column('bid', 'actual_price')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('bid', sa.Column('actual_price', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('bid', 'actual_amount')
    # ### end Alembic commands ###