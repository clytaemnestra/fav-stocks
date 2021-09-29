"""empty message

Revision ID: a170f14a70e8
Revises: 3756e01fd53d
Create Date: 2021-09-28 22:35:14.158130

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a170f14a70e8'
down_revision = '3756e01fd53d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('transaction_type')
    op.drop_constraint('transaction_transaction_type_id_fkey', 'transaction', type_='foreignkey')
    op.drop_column('transaction', 'transaction_type_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('transaction', sa.Column('transactiontype_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.create_foreign_key('transaction_transactiontype_id_fkey', 'transaction', 'transactiontype', ['transactiontype_id'], ['id'])
    op.create_table('transactiontype',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('type', postgresql.ENUM('buy', 'sell', name='transactiontypespostgresenum'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transactiontype_pkey')
    )
    # ### end Alembic commands ###
