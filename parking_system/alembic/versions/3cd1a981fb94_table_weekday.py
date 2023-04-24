"""Table WeekDay

Revision ID: 3cd1a981fb94
Revises: 6773ebd35c95
Create Date: 2023-04-22 16:13:29.832166

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3cd1a981fb94'
down_revision = '6773ebd35c95'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weekday',
    sa.Column('id_day', sa.String(length=4), nullable=False),
    sa.Column('day', sa.Enum('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday', name='day_of_week_enum'), nullable=False),
    sa.Column('id_reservation', sa.String(length=4), nullable=True),
    sa.Column('start_time', sa.Time(), nullable=False),
    sa.Column('end_time', sa.Time(), nullable=False),
    sa.ForeignKeyConstraint(['id_reservation'], ['reservation.id_reservation'], ),
    sa.PrimaryKeyConstraint('id_day')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weekday')
    # ### end Alembic commands ###