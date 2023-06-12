"""create post table

Revision ID: 693210bf9cef
Revises: 
Create Date: 2023-06-11 19:17:35.447422

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '693210bf9cef'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False,
                    primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    ob.drop_table('posts')
    pass
