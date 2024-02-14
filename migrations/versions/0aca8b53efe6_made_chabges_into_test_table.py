"""made chabges into test table

Revision ID: 0aca8b53efe6
Revises: 76b49a3dfe9a
Create Date: 2024-02-14 16:04:02.130826

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0aca8b53efe6'
down_revision = '76b49a3dfe9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.add_column(sa.Column('username', sa.String(length=64), nullable=False))
        batch_op.create_index(batch_op.f('ix_test_username'), ['username'], unique=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('test', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_test_username'))
        batch_op.drop_column('username')

    # ### end Alembic commands ###
