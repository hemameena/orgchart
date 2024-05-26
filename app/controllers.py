from flask import render_template, Blueprint
from .services import get_team_members

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    team_members = [member.to_dict() for member in get_team_members()]
    return render_template('index.html', team_members=team_members)

@main_bp.route('/index1')
def index1():
    team_members = [member.to_dict() for member in get_team_members()]
    return render_template('index1.html', team_members=team_members)

@main_bp.route('/index2')
def index2():
    team_members = [member.to_dict() for member in get_team_members()]
    return render_template('index2.html', team_members=team_members)

def register_blueprints(app):
    app.register_blueprint(main_bp)
