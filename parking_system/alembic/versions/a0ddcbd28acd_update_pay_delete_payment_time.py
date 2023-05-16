"""Update pay: delete payment time

Revision ID: a0ddcbd28acd
Revises: 6b691bc02a6e
Create Date: 2023-05-14 19:20:17.248012

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a0ddcbd28acd'
down_revision = '6b691bc02a6e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pay', sa.Column('payment_datetime', sa.DateTime(), nullable=True))
    op.drop_column('pay', 'payment_time')
    op.drop_column('pay', 'payment_date')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pay', sa.Column('payment_date', mysql.DATETIME(), nullable=False))
    op.add_column('pay', sa.Column('payment_time', mysql.TIME(), nullable=False))
    op.drop_column('pay', 'payment_datetime')
    # ### end Alembic commands ###
