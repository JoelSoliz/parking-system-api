"""changes notification

Revision ID: 7a344904b341
Revises: e09643fdb2b7
Create Date: 2023-04-11 06:00:42.321107

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '7a344904b341'
down_revision = 'e09643fdb2b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('notification', sa.Column('notification_type', sa.Enum('Whatsapp', 'Email'), nullable=True))
    op.alter_column('notification', 'request_date',
               existing_type=mysql.DATETIME(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('notification', 'request_date',
               existing_type=mysql.DATETIME(),
               nullable=False)
    op.drop_column('notification', 'notification_type')
    # ### end Alembic commands ###