"""empty message

Revision ID: bfb0eebab57c
Revises: 71c29b5d1263
Create Date: 2021-12-05 16:28:17.946056

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bfb0eebab57c'
down_revision = '71c29b5d1263'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('draft', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'draft')
    # ### end Alembic commands ###
