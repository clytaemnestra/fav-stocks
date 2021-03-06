"""empty message

Revision ID: f4b76e18c82f
Revises: abae7bc26069
Create Date: 2021-08-20 12:24:40.826302

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f4b76e18c82f"
down_revision = "abae7bc26069"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "transaction_type",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "type", sa.Enum("BUY", "SELL", name="transactiontypesenum"), nullable=False
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("transaction_type")
    # ### end Alembic commands ###
