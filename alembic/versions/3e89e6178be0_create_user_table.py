"""create user table

Revision ID: 3e89e6178be0
Revises: 
Create Date: 2020-12-30 11:14:37.997289

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3e89e6178be0'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
          op.create_table(
        'account',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(110), nullable=False),
        sa.Column('email', sa.String(110), nullable=False, unique=True),
        sa.Column('hashed_password', sa.String(110), nullable=False),
        sa.Column('confirm_password', sa.String(110), nullable=False),
        sa.Column('phone', sa.String(110)),
        sa.Column('dateofbirth', sa.DateTime),
        sa.Column('is_active', sa.Boolean),
        sa.Column('create_date', sa.DateTime),
    )


def downgrade():
    pass
