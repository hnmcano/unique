"""adição da coluna opcores de pagamento

Revision ID: df05498898df
Revises: c176464eb3cc
Create Date: 2026-03-09 22:44:41.576316

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'df05498898df'
down_revision: Union[str, None] = 'c176464eb3cc'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
