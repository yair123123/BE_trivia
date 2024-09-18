from dataclasses import asdict
from flask import blueprints, jsonify, request

from repository.user_repository import *
user_blueprint = blueprints.Blueprint('user', __name__)

@user_blueprint.route('/', methods=['GET'])
def findAll():
    users = list(map(asdict, getAll()))
    return jsonify(users),200
@user_blueprint.route('/{id}', methods=['GET'])
def findById(id:int):
    user = asdict(getById(id))
    return jsonify(user),200

@user_blueprint.route('/create', methods=['POST'])
def create_user():
    a = request.json
    user = User(**a)
    id = create(user)
    return jsonify(id),201
@user_blueprint.route('/{id}', methods=['PUT'])
def update(id:int):
    a = request.json()
    new_user = User(**a)
    new_user = update(new_user,id)
    return jsonify(new_user),200
@user_blueprint.route('/{id}', methods=['DELETE'])
def delete(id:int):
    delete(id)
    return jsonify({}),200