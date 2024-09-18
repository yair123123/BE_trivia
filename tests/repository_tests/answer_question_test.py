import pytest

from models.Answer import Answer
from models.Question import Question
from repository.database import create_tables, get_db_connection, drop_all_tables
from repository import answers_repository as a
from repository import question_repository as q


@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    yield
    drop_all_tables()

def test_create(setup_database):
    question = Question("a","a","a","a")
    question_id = q.create(question)
    answer = Answer(question_id,"b",True)
    answer_id = a.create(answer)
    assert q.findById(question_id).text_question == question.text_question
    assert a.findById(answer_id).text_answer == answer.text_answer
def test_delete(setup_database):
    question = Question("a","a","a","a")
    question_id = q.create(question)
    answer = Answer(question_id,"b",True)
    answer_id = a.create(answer)
    a.delete(answer_id)
    q.delete(question_id)
    assert a.findById(answer_id) is None
    assert q.findById(question_id) is None
def test_update(setup_database):
    question = Question("a","a","a","a")
    question_id = q.create(question)
    answer = Answer(question_id,"b",True)
    answer_id = a.create(answer)

    new_question = Question("checkingUpdate","checking","checking","a")
    new_answer = Answer(question_id,"checkingUpdate",True)
    new_question_after_update = q.update(new_question,question_id)
    new_answer_after_update = a.update(new_answer,answer_id)
    assert new_question_after_update.text_question == new_question.text_question
    assert new_answer_after_update.text_answer == new_answer.text_answer
