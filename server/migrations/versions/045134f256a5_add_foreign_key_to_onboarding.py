"""add foreign key to onboarding

Revision ID: 045134f256a5
Revises: 5991709c659d
Create Date: 2025-01-17 15:56:15.676695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '045134f256a5'
down_revision = '5991709c659d'
branch_labels = None
depends_on = None


def upgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.add_column(sa.Column('employee_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(
            'fk_onboardings_employee_id_employees', 'employees', ['employee_id'], ['id']
        )


def downgrade():
    # Use batch mode for SQLite compatibility
    with op.batch_alter_table('onboardings', schema=None) as batch_op:
        batch_op.drop_constraint('fk_onboardings_employee_id_employees', type_='foreignkey')
        batch_op.drop_column('employee_id')
