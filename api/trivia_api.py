
from typing import List, Dict

import requests
from toolz import pipe
from toolz.curried import  pluck, partial

from models.Answer import Answer
from models.Question import Question
from models.User import User


def get_from_api(url):
    response = requests.get(url)
    return response.json()

def get_questions_and_answers() -> List[Dict[str, str]]:
    questions_and_answers = get_from_api("https://opentdb.com/api.php?amount=20")
    # if questions_and_answers['response_code'] == 5:
    #     return get_questions_and_answers()
    return pipe(
        questions_and_answers,
        lambda x: x['results'],
    )

