"""Add created index to markers table

Revision ID: 2c54437f4ee4
Revises: 6b5383680e26
Create Date: 2020-08-12 09:05:44.177123

"""

# revision identifiers, used by Alembic.

revision = '2c54437f4ee4'
down_revision = '6b5383680e26'
branch_labels = None
depends_on = None

from alembic import op

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###

    op.create_index('idx_markers_created', 'markers', ['created'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('idx_markers_created', table_name='markers')
    # ### end Alembic commands ###