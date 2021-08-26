"""empty message

Revision ID: b097c273802b
Revises: 103291394e89
Create Date: 2021-08-19 22:25:28.798657

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b097c273802b'
down_revision = '103291394e89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction_type', sa.Column('type', sa.Enum('buy', 'sell', name='transaction_types'), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('transaction_type', 'type')
    # ### end Alembic commands ###
