"""s

Revision ID: e3d49e0603d6
Revises: efd86b945e49
Create Date: 2023-07-29 17:06:12.805131

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e3d49e0603d6'
down_revision = 'efd86b945e49'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('support',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('bank_id', sa.Integer(), nullable=True),
    sa.Column('university_id', sa.Integer(), nullable=True),
    sa.Column('is_test', sa.Boolean(), nullable=True),
    sa.Column('url', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['bank_id'], ['bank.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_support_bank_id'), 'support', ['bank_id'], unique=False)
    op.create_index(op.f('ix_support_id'), 'support', ['id'], unique=False)
    op.create_index(op.f('ix_support_university_id'), 'support', ['university_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_support_university_id'), table_name='support')
    op.drop_index(op.f('ix_support_id'), table_name='support')
    op.drop_index(op.f('ix_support_bank_id'), table_name='support')
    op.drop_table('support')
    # ### end Alembic commands ###
