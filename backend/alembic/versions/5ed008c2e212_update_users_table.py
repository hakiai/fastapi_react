"""update users table

Revision ID: 5ed008c2e212
Revises: 9c05b3029618
Create Date: 2021-06-15 07:58:20.407249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ed008c2e212'
down_revision = '9c05b3029618'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('password', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('e_mail', sa.String(length=255), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'e_mail')
    op.drop_column('users', 'password')
    op.drop_column('users', 'name')
    # ### end Alembic commands ###
