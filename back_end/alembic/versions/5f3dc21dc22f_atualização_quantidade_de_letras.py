"""Atualização quantidade de letras

Revision ID: 5f3dc21dc22f
Revises: 6e4d48046b29
Create Date: 2025-10-12 15:14:25.078133

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5f3dc21dc22f'
down_revision: Union[str, None] = '6e4d48046b29'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
