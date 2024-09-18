from typing import List, Dict

from toolz import pipe,partial

from api.trivia_api import get_questions_and_answers
from models.Answer import Answer
from models.Question import Question
from repository import question_repository, answers_repository


def get_all_question_and_answers() -> List[Dict[str, str]]:
    a = list(get_questions_and_answers())
    return a

def save_all(all_question_and_answers):
    for x in all_question_and_answers:
        question =Question(
            text_question=x['question'],
            type=x['type'],
            difficulty=x['difficulty'],
                 category=x['category']
        )
        id_question = question_repository.create(question)
        answers_correct = Answer(text_answer= x['correct_answer'],
                                 correct=True,
                                 question_id=id_question
        )
        answers_incorrect = list(map(lambda x: Answer(text_answer=x, correct=False, question_id=id_question),x['incorrect_answers']))
        list(map(answers_repository.create,answers_incorrect))
        answers_repository.create(answers_correct)

def get_all_questionsAnswers_and_save():
    questionsAnswers = get_all_question_and_answers()
    save_all(questionsAnswers)