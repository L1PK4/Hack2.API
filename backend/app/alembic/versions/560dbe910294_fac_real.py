"""fac real

Revision ID: 560dbe910294
Revises: c553702d74c9
Create Date: 2023-07-28 20:11:45.474623

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '560dbe910294'
down_revision = 'c553702d74c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('faculty',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('university_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['university_id'], ['university.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_faculty_id'), 'faculty', ['id'], unique=False)
    op.create_index(op.f('ix_faculty_university_id'), 'faculty', ['university_id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_faculty_university_id'), table_name='faculty')
    op.drop_index(op.f('ix_faculty_id'), table_name='faculty')
    op.drop_table('faculty')
    # ### end Alembic commands ###
