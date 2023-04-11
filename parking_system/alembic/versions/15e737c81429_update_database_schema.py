"""update database schema

Revision ID: 15e737c81429
Revises: 4d26e56178f5
Create Date: 2023-04-10 18:53:45.777832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15e737c81429'
down_revision = '4d26e56178f5'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role_permission',
    sa.Column('id_role_permission', sa.String(length=4), nullable=False),
    sa.Column('id_role', sa.String(length=4), nullable=True),
    sa.Column('id_permission', sa.String(length=4), nullable=True),
    sa.ForeignKeyConstraint(['id_permission'], ['permission.id_permission'], ),
    sa.ForeignKeyConstraint(['id_role'], ['role.id_role'], ),
    sa.PrimaryKeyConstraint('id_role_permission')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('role_permission')
    # ### end Alembic commands ###
