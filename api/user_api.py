
from typing import List
import requests
from toolz import pipe
from toolz.curried import  pluck, partial

from models.User import User


def get_from_api(url):
    response = requests.get(url)
    return response.json()

def get_users() -> List[User]:
    users = get_from_api("https://randomuser.me/api?results=4")
    return pipe(
        users,
        lambda x: x['results'],
        partial(map, lambda x: User(
            first=x['name']['first'],
            last=x['name']['last'],
            email=x['email']
        )),
    )

