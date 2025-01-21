from sqlalchemy import Table, Column, Integer, String
from db import metadata


users = Table(
    "users",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String(30), unique=True, nullable=False),
    Column("password_hash", String, nullable=False),
    Column("age", Integer),
)

pets = Table(
    "pets",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("age", String, nullable=False),
    Column("species", String, nullable=False),
    Column("breed", String, nullable=False)
)
