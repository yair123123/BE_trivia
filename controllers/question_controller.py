from dataclasses import asdict
from flask import blueprints, jsonify, request

from models.Question import Question
from repository import question_repository as re
from repository import answers_repository as an

question_blueprint = blueprints.Blueprint('question', __name__)

@question_blueprint.route('/',methods=['GET'])
def findAll():
    questions = list(map(asdict, re.findAll()))
    return jsonify(questions),200

@question_blueprint.route('/<int:id>',methods=['GET'])
def findById(id:int):
    question = asdict(re.findById(id))
    return jsonify(question),200
@question_blueprint.route('/create', methods=['POST'])
def create():
    a = request.json
    question = Question(**a)
    id = re.create(question)
    return jsonify(id),201
@question_blueprint.route('/{id}', methods=['GET'])
def update(id:int):
    a = request.json
    question = Question(**a)
    new_update = re.update(question,id)
    return jsonify(new_update),200
@question_blueprint.route('/{id}', methods=['GET'])
def delete(id:int):
    re.delete(id)
    return jsonify({}),200
@question_blueprint.route('answers/<int:id>', methods=['GET'])
def get_answers_by_question(id:int):
    answers = list(map(lambda x:asdict(x),an.find_by_question_id(id)))
    return jsonify(answers),200