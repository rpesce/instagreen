"""Instagram account table

Revision ID: 730aa1922257
Revises: bc08661fba56
Create Date: 2020-06-14 23:22:56.864949

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '730aa1922257'
down_revision = 'bc08661fba56'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instagram_account',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('instagram_username', sa.String(length=500), nullable=True),
    sa.Column('instagram_password', sa.String(length=500), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instagram_account')
    # ### end Alembic commands ###
