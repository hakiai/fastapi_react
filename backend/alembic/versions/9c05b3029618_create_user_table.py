"""create user table

Revision ID: 9c05b3029618
Revises:
Create Date: 2021-06-14 06:44:11.744292

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9c05b3029618'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
    )


def downgrade():
    op.drop_table('users')
