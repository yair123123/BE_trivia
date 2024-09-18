from flask import jsonify

from models.Question import Question
from repository.database import get_db_connection


def findAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM questions
            """      )
        rows = cursor.fetchall()
        questions = [Question(**f) for f in rows]
        return questions


def findById(question_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM questions WHERE id = %s", (question_id,))
        question = cursor.fetchone()
        if question is None:
            return None
        question = Question(**question)
        return question

def create(question:Question) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO questions (text_question,type,difficulty,category) VALUES (%s,%s,%s,%s) RETURNING id
            """,
            (question.text_question,question.type,question.difficulty,question.category)
        )
        connection.commit()
        question_id = cursor.fetchone()["id"]
        return question_id
def update(question:Question,id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE questions SET 
            text_question = %s,
            type = %s,
            difficulty = %s,
            category = %s
              WHERE id = %s
            """,
            (question.text_question, question.type, question.difficulty, question.category, id)
        )
        connection.commit()
        return findById(id)

def delete(question_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM questions where id = %s
            """
            , (question_id,)
        )
        connection.commit()