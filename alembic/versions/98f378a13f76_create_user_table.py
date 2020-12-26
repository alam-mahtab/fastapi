"""Create user table

Revision ID: 98f378a13f76
Revises: 
Create Date: 2020-12-24 11:01:22.277637

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '98f378a13f76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
         op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True, unique=True),
        sa.Column('username', sa.String(100), nullable=False, unique=True),
        sa.Column('first_name', sa.String(100), nullable=False),
        sa.Column('last_name', sa.String(100), nullable=False),
        sa.Column('dateofbirth', sa.DateTime),
        sa.Column('phone', sa.String),
       
        sa.Column('hashed_password', sa.String(100)),
        sa.Column('email', sa.String(200)),
        sa.Column('create_date', sa.DateTime),
        sa.Column('is_active', sa.Boolean),
        
    )



def downgrade():
    pass
