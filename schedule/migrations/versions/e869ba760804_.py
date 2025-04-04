"""empty message

Revision ID: e869ba760804
Revises: 
Create Date: 2025-03-30 16:16:34.370117

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e869ba760804'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('categories',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('category_father', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['category_father'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=True),
    sa.Column('end_time', sa.Time(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('done', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('recurring_activities',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=False),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=True),
    sa.Column('end_date', sa.Date(), nullable=True),
    sa.Column('category', sa.Integer(), nullable=True),
    sa.Column('day_of_week', sa.Integer(), nullable=True),
    sa.Column('day_of_month', sa.Integer(), nullable=True),
    sa.Column('day_of_year', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['category'], ['categories.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('recurring_activities')
    op.drop_table('activities')
    op.drop_table('categories')
    # ### end Alembic commands ###
