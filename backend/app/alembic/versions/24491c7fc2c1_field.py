"""field

Revision ID: 24491c7fc2c1
Revises: d0f2c12a65e8
Create Date: 2023-07-29 06:30:38.582844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '24491c7fc2c1'
down_revision = 'd0f2c12a65e8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('field',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('faculty_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['faculty_id'], ['faculty.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_field_faculty_id'), 'field', ['faculty_id'], unique=False)
    op.create_index(op.f('ix_field_id'), 'field', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_field_id'), table_name='field')
    op.drop_index(op.f('ix_field_faculty_id'), table_name='field')
    op.drop_table('field')
    # ### end Alembic commands ###
