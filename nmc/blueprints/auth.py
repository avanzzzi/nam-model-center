from flask import Blueprint, jsonify

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/test', methods=['GET'])
def test():
    return jsonify(message='Test Ok'), 200
