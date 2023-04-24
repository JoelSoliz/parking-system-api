"""Table Changed ParkingSpot column section

Revision ID: ca870c0a8cae
Revises: 1b984359d781
Create Date: 2023-04-24 11:04:57.704746

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ca870c0a8cae'
down_revision = '1b984359d781'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parking_spot', sa.Column('section', sa.String(length=20), nullable=False))
    op.alter_column('parking_spot', 'coordinate',
               existing_type=mysql.TEXT(collation='utf8mb4_spanish2_ci'),
               nullable=False)
    op.drop_column('parking_spot', 'description')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('parking_spot', sa.Column('description', mysql.VARCHAR(collation='utf8mb4_spanish2_ci', length=200), nullable=False))
    op.alter_column('parking_spot', 'coordinate',
               existing_type=mysql.TEXT(collation='utf8mb4_spanish2_ci'),
               nullable=True)
    op.drop_column('parking_spot', 'section')
    # ### end Alembic commands ###
