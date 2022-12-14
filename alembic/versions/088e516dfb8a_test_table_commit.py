"""Test table commit

Revision ID: 088e516dfb8a
Revises: 
Create Date: 2022-10-15 20:38:22.374711

"""
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

from alembic import op

# revision identifiers, used by Alembic.
revision = "088e516dfb8a"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "test_table", "created", existing_type=postgresql.TIMESTAMP(), nullable=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "test_table", "created", existing_type=postgresql.TIMESTAMP(), nullable=True
    )
    # ### end Alembic commands ###
