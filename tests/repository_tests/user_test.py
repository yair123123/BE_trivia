import pytest
from models.User import User
from repository.database import create_tables, get_db_connection, drop_all_tables
from repository.user_repository import *



@pytest.fixture(scope='module')
def setup_database():
    create_tables()
    yield
    drop_all_tables()


def test_create_user(setup_database):
    user_check = User("checking","checking","checking")
    id = create(user_check)
    assert getById(id).first == user_check.first
def test_delete_user(setup_database):
    user_check = User("checking","checking","checking")
    id = create(user_check)
    delete(id)
    assert getById(id) is None
def test_update(setup_database):
    user_check = User("checking","checking","checking")
    id = create(user_check)
    new_user = User("checkingUpdate","checking","checking")
    new_user_after_update = update(new_user,id)
    assert new_user_after_update.first == new_user.first
