"""empty message

Revision ID: b6032e0a017e
Revises: 53c85bee9f11
Create Date: 2021-08-20 01:25:02.446930

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "b6032e0a017e"
down_revision = "53c85bee9f11"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "transaction_type",
        "type",
        existing_type=postgresql.ENUM("BUY", "SELL", name="transactiontypes"),
        nullable=False,
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "transaction_type",
        "type",
        existing_type=postgresql.ENUM("BUY", "SELL", name="transactiontypes"),
        nullable=True,
    )
    # ### end Alembic commands ###
