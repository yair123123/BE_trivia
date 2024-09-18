from repository.database import create_tables
from services.trivia_service import get_all_questionsAnswers_and_save
from services.user_service import get_users_and_save


def start():
        create_tables()
        get_all_questionsAnswers_and_save()
        get_users_and_save()
