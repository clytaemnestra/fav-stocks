"""empty message

Revision ID: d5867fcc7e14
Revises: b662eadab8cd
Create Date: 2021-09-29 17:02:14.833839

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd5867fcc7e14'
down_revision = 'b662eadab8cd'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('account', 'test_field')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('account', sa.Column('test_field', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###