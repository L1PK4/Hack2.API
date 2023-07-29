"""offer

Revision ID: 359fed40e8ab
Revises: bd917cb2c08c
Create Date: 2023-07-29 09:44:39.899581

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '359fed40e8ab'
down_revision = 'bd917cb2c08c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('offer',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('min_price', sa.Integer(), nullable=True),
    sa.Column('max_price', sa.Integer(), nullable=True),
    sa.Column('percent', sa.Integer(), nullable=True),
    sa.Column('annual_payment', sa.Integer(), nullable=True),
    sa.Column('payment_term', sa.Integer(), nullable=True),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['bank_id'], ['bank.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_offer_id'), 'offer', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_offer_id'), table_name='offer')
    op.drop_table('offer')
    # ### end Alembic commands ###