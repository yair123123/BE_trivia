from typing import List

from api.user_api import get_users
from models.User import User
from repository.user_repository import create, getAll


def get_users_from_api() -> List[User]:
    users = get_users()
    return users
def save_users(users : List[User]) -> List[int]:
    users = list(users)
    ids = list(map(create,users))
    return ids
def get_users_and_save():
    users = get_users_from_api()
    save_users(users)
def print_users():
    all_users = getAll()
    for i in range(len(all_users)):
        print(f"{all_users[i].id}: {all_users[i].first} {all_users[i].last}")