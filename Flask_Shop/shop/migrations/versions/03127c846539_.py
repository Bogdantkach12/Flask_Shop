"""empty message

Revision ID: 03127c846539
Revises: 26518ff59844
Create Date: 2024-06-03 19:58:51.415134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03127c846539'
down_revision = '26518ff59844'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'login',
               existing_type=sa.VARCHAR(length=25),
               nullable=False)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    op.alter_column('user', 'password_confirmation',
               existing_type=sa.VARCHAR(length=20),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password_confirmation',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=20),
               nullable=True)
    op.alter_column('user', 'email',
               existing_type=sa.VARCHAR(length=255),
               nullable=True)
    op.alter_column('user', 'login',
               existing_type=sa.VARCHAR(length=25),
               nullable=True)
    # ### end Alembic commands ###