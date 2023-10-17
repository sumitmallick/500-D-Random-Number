from flask import Blueprint, request, jsonify
from .random_array_generator import generate_random_array

api_blueprint = Blueprint('api', __name__)


@api_blueprint.route('/generate_random_array', methods=['POST'])
def generate_random_array_endpoint():
  try:
    data = request.get_json()
    sentence = data.get('sentence', '')
    random_array = generate_random_array()
    response = {'sentence': sentence, 'random_array': random_array}
    return jsonify(response), 200
  except Exception as e:
    return jsonify({'error': str(e)}), 500
