"""empty message

Revision ID: bc65dc1211bf
Revises: 86e59190238d
Create Date: 2021-08-25 23:54:18.644164

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'bc65dc1211bf'
down_revision = '86e59190238d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('type', sa.Enum('BUY', 'SELL', name='transactiontypespostgresenum'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('transaction_types')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('transaction_types',
    sa.Column('id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('type', postgresql.ENUM('buy', 'sell', name='transactiontypes'), autoincrement=False, nullable=True)
    )
    op.drop_table('transaction_type')
    # ### end Alembic commands ###