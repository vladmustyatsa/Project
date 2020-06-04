"""empty message

Revision ID: 69eb18a0653b
Revises: f5aef320e306
Create Date: 2020-04-23 20:10:23.874845

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69eb18a0653b'
down_revision = 'f5aef320e306'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project', sa.Column('avatar', sa.String(length=100), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project', 'avatar')
    # ### end Alembic commands ###