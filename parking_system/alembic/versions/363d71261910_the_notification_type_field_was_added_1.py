"""the notification type field was added 1

Revision ID: 363d71261910
Revises: e09643fdb2b7
Create Date: 2023-04-15 22:07:42.346768

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '363d71261910'
down_revision = 'e09643fdb2b7'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('notification_type', sa.Enum('Whatsapp', 'Email'), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer', 'notification_type')
    # ### end Alembic commands ###