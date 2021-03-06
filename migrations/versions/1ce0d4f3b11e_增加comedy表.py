"""增加comedy表

Revision ID: 1ce0d4f3b11e
Revises: 4e0aceaaa8f7
Create Date: 2016-11-29 22:59:37.404280

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1ce0d4f3b11e'
down_revision = '4e0aceaaa8f7'
branch_labels = None
depends_on = None


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('comedy',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('score', sa.Integer(), nullable=True),
    sa.Column('reviews', sa.Integer(), nullable=True),
    sa.Column('information', sa.Integer(), nullable=True),
    sa.Column('cover_url', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comedy')
    ### end Alembic commands ###
