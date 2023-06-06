"""update reservation_assignment: assisted_datetime

Revision ID: 15eb9b64b58a
Revises: 13750bb1eaed
Create Date: 2023-05-29 16:20:42.750505

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15eb9b64b58a'
down_revision = '13750bb1eaed'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('reservation_assignment', sa.Column('assisted_datetime', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('reservation_assignment', 'assisted_datetime')
    # ### end Alembic commands ###