from flask import jsonify

from models.UserAnswer import UserAnswer
from repository.database import get_db_connection


def findAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM user_answers
            """      )
        rows = cursor.fetchall()
        user_answers = [UserAnswer(**f) for f in rows]
        return user_answers


def findById(user_answers_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM user_answers WHERE id = %s", (user_answers_id,))
        user_answer = cursor.fetchone()
        user_answer = UserAnswer(**user_answer)
        return user_answer

def create(user_answer:UserAnswer) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO user_answers (user_id,question_id,answer_text,is_correct,time_taken) VALUES (%s,%s,%s,%s,%s) RETURNING id
            """,
            (user_answer.user_id,user_answer.question_id,user_answer.answer_text,user_answer.is_correct,user_answer.time_taken)
        )
        connection.commit()
        user_answers_id = cursor.fetchone()[0]
        return user_answers_id
def update(user_answer:UserAnswer):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE user_answers SET
             user_id = %s,
            question_id = %s,
            answer_text = %s,
            is_correct = %s,
            time_taken = %s
             WHERE id = %s
            """,
            (user_answer.user_id,user_answer.question_id,user_answer.answer_text,user_answer.is_correct,user_answer.time_taken,user_answer.id)
        )
        connection.commit()
        return findById(user_answer.id)

def delete(id : int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM user_answers where id = %s
            """
            , (id,)
        )
        connection.commit()