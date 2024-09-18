from flask import jsonify

from models.User import User
from repository.database import get_db_connection


def getAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM users
            """      )
        rows = cursor.fetchall()
        users = [User(**f) for f in rows]
        return users


def getById(user_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        if user is None:
            return None
        user = User(**user)
        return user

def create(user:User) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO users (first,last,email) VALUES (%s,%s,%s) RETURNING id
            """,
            (user.first,user.last,user.email)
        )
        connection.commit()
        user_id = cursor.fetchone()["id"]
        return user_id
def update(user:User,user_id):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE users SET first = %s, last = %s, email = %s WHERE id = %s
            """,
            (user.first,user.last,user.email, user_id)
        )
        connection.commit()
        return getById(user_id)

def delete(id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM users WHERE id = %s
            """,
            (id,)
        )
        connection.commit()