"""Atualização quantidade de letras

Revision ID: adcf0b209cb7
Revises: 5f3dc21dc22f
Create Date: 2025-10-12 15:14:44.814586

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'adcf0b209cb7'
down_revision: Union[str, None] = '5f3dc21dc22f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
