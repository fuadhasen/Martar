"""create the models

Revision ID: 7d975a3c1642
Revises: 
Create Date: 2025-01-04 11:28:58.854065

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision: str = '7d975a3c1642'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('trip',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('origin', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('destination', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('trip_date', sa.DateTime(), nullable=False),
    sa.Column('price', sa.Float(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('full_name', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('email', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=False),
    sa.Column('password', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('phone_number', sqlmodel.sql.sqltypes.AutoString(length=15), nullable=True),
    sa.Column('role', sa.Enum('tourist', 'driver', name='roleenum'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('driver',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('vehicle_type', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('vehicle_registration_number', sqlmodel.sql.sqltypes.AutoString(length=50), nullable=False),
    sa.Column('languages_spoken', sqlmodel.sql.sqltypes.AutoString(length=255), nullable=True),
    sa.Column('experience_years', sa.Integer(), nullable=True),
    sa.Column('verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('vehicle_registration_number')
    )
    op.create_table('booking',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('driver_id', sa.Uuid(), nullable=False),
    sa.Column('trip_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('number_of_passengers', sa.Integer(), nullable=False),
    sa.Column('total_price', sa.Float(), nullable=False),
    sa.Column('booking_date', sa.DateTime(), nullable=False),
    sa.Column('status', sqlmodel.sql.sqltypes.AutoString(length=20), nullable=False),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
    sa.ForeignKeyConstraint(['trip_id'], ['trip.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('review',
    sa.Column('id', sa.Uuid(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('driver_id', sa.Uuid(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('rating', sa.Integer(), nullable=False),
    sa.Column('comment', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.ForeignKeyConstraint(['driver_id'], ['driver.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('review')
    op.drop_table('booking')
    op.drop_table('driver')
    op.drop_table('user')
    op.drop_table('trip')
    # ### end Alembic commands ###
