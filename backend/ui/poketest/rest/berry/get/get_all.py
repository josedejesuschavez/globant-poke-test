from flask import Blueprint


blueprint = Blueprint('get_all_berries', __name__)

@blueprint.route('/get-all', methods=['GET'])
def get_all():
    return '<p>Log In</p>'