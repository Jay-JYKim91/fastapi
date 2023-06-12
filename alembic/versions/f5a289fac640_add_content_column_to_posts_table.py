"""add content column to posts table

Revision ID: f5a289fac640
Revises: 693210bf9cef
Create Date: 2023-06-11 19:25:14.740232

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f5a289fac640'
down_revision = '693210bf9cef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade() -> None:
    op.drop_column('posts', 'content')
    pass
