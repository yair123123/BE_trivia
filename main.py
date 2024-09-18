import os

from flask import jsonify , Flask
from controllers.user_controller import user_blueprint
from controllers.question_controller import question_blueprint
from services.main_service import start
from services.user_service import print_users

app =Flask(__name__)

# print("Choice user?")
# print_users()


def create_app():
    app = Flask(__name__)
    app.register_blueprint(user_blueprint, url_prefix='/api/user')
    app.register_blueprint(question_blueprint, url_prefix='/api/question')

    if os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        start()

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)