from flask import jsonify
from models.Answer import Answer
from repository.database import get_db_connection


def findAll():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            SELECT * FROM answers
            """      )
        rows = cursor.fetchall()
        answers = [Answer(**f) for f in rows]
        return answers


def findById(answer_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM answers WHERE answer_id = %s", (answer_id,))
        d = cursor.fetchone()
        if d is None:
            return None
        answer = Answer(**d)
        return answer

def create(answer:Answer) -> int:
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO answers (question_id,text_answer,correct) VALUES (%s,%s,%s) RETURNING answer_id
            """,
            (answer.question_id,answer.text_answer,answer.correct)
        )
        connection.commit()
        answer_id = cursor.fetchone()["answer_id"]
        return answer_id
def update(answer:Answer,id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            UPDATE answers SET text_answer = %s,
            correct = %s,
            question_id = %s
              WHERE answer_id = %s
            """,
            (answer.text_answer, answer.correct, answer.question_id, id)
        )
        connection.commit()
        return findById(id)

def delete(id : int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(
            """
            DELETE FROM answers WHERE answer_id = %s
            """,
            (id,)
        )
        connection.commit()
def find_by_question_id(question_id:int):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute("SELECT * FROM answers WHERE question_id = %s", (question_id,))
        d = cursor.fetchall()
        if d is None:
            return None
        answers = list(map(lambda x: Answer(**x),d))
        return answers