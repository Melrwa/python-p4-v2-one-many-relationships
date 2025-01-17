"""add foreign key to Review

Revision ID: 5991709c659d
Revises: b9edb9db2d6a
Create Date: 2025-01-17 15:27:19.602919

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import sqlite

# revision identifiers, used by Alembic.
revision = '5991709c659d'
down_revision = 'b9edb9db2d6a'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_reviews_employee_id_employees', 'employees', ['employee_id'], ['id']
        )


def downgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_constraint('fk_reviews_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
