"""univ1

Revision ID: d0f2c12a65e8
Revises: 13362fdb3510
Create Date: 2023-07-29 05:28:05.842940

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0f2c12a65e8'
down_revision = '13362fdb3510'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('university', sa.Column('url', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('university', 'url')
    # ### end Alembic commands ###
