"""empty message

Revision ID: 0f2e43731d1e
Revises: 1c09fe4710a5
Create Date: 2020-07-21 20:48:33.804578

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0f2e43731d1e'
down_revision = '1c09fe4710a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('project_user_request', sa.Column('positive_status', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('project_user_request', 'positive_status')
    # ### end Alembic commands ###
