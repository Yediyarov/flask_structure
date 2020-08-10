"""empty message

Revision ID: 94ce88e5cbae
Revises: 4911d5cba8b4
Create Date: 2020-07-18 04:57:35.022672

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '94ce88e5cbae'
down_revision = '4911d5cba8b4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('id')
    )
    op.create_table('post',
    sa.Column('id', sqlalchemy_utils.types.uuid.UUIDType(binary=False), nullable=False),
    sa.Column('created_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(), server_default=sa.text('now()'), nullable=True),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('content', sa.String(), nullable=True),
    sa.Column('user_id', sqlalchemy_utils.types.uuid.UUIDType(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_unique_constraint(None, 'cars', ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'cars', type_='unique')
    op.drop_table('post')
    op.drop_table('user')
    # ### end Alembic commands ###
