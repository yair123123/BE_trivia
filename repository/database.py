import psycopg2
from psycopg2.extras import RealDictCursor
from config.sql_config import SQLALCHEMY_DATABASE_URI


def get_db_connection():
    return psycopg2.connect(SQLALCHEMY_DATABASE_URI,cursor_factory=RealDictCursor)
def create_tables():
    with get_db_connection() as conn , conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            first varchar(100) NOT NULL,
            last varchar(100) NOT NULL,
            email varchar(100) NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS questions (
            id SERIAL PRIMARY KEY,
            text_question text NOT NULL,
            type varchar(100) NOT NULL,
            difficulty varchar(100) NOT NULL,
            category varchar(100) NOT NULL
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS answers (
            answer_id SERIAL PRIMARY KEY,
            question_id int NOT NULL,
            text_answer text NOT NULL,
            correct boolean NOT NULL,
            FOREIGN KEY(question_id) REFERENCES questions(id) ON DELETE CASCADE
        );
        """)

        cur.execute("""
        CREATE TABLE IF NOT EXISTS user_answers (
            id SERIAL PRIMARY KEY,
            user_id int NOT NULL,
            question_id int NOT NULL,
            answer_text varchar(100) NOT NULL,
            is_correct boolean NOT NULL,
            time_taken INT NOT NULL,
            FOREIGN KEY(user_id) REFERENCES users(id) ON DELETE CASCADE, 
            FOREIGN KEY(question_id) REFERENCES questions(id) ON DELETE CASCADE
        );
        """)
        conn.commit()

def drop_all_tables():
    with get_db_connection() as conn, conn.cursor() as cur:
        try:
            cur.execute("DROP TABLE IF EXISTS users,questions,answers,user_answers")
        except:
            drop_all_tables()
        conn.commit()