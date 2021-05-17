"""Replication lifetimes

Revision ID: 5ad28ad61416
Revises: 9372814239d7
Create Date: 2021-04-21 11:27:04.309390+00:00

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5ad28ad61416'
down_revision = '9372814239d7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('storage_replication', schema=None) as batch_op:
        batch_op.add_column(sa.Column('repl_lifetimes', sa.TEXT(), nullable=True))

    op.execute("UPDATE storage_replication SET repl_lifetimes = '[]'")

    with op.batch_alter_table('storage_replication', schema=None) as batch_op:
        batch_op.alter_column('repl_lifetimes', existing_type=sa.TEXT(), nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('storage_replication', schema=None) as batch_op:
        batch_op.drop_column('repl_lifetimes')

    # ### end Alembic commands ###