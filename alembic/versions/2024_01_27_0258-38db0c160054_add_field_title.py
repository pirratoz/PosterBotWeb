"""add field title

Revision ID: 38db0c160054
Revises: b7f425a2784f
Create Date: 2024-01-27 02:58:50.582357

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '38db0c160054'
down_revision: Union[str, None] = 'b7f425a2784f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('templates', sa.Column('title', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('templates', 'title')
    # ### end Alembic commands ###
