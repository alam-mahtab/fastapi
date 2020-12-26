"""create account table

Revision ID: d0151613f2b5
Revises: d87438b108e2
Create Date: 2020-12-24 19:24:13.475367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0151613f2b5'
down_revision = 'd87438b108e2'
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
