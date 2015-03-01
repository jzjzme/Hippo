from flask import request, jsonify
from flask.views import MethodView
from flask.ext.login import current_user, login_user, logout_user

from server.models.users import User

from server import app, db, login_manager



def session_auth_required(func):
    def decorated(*args, **kwargs):
        if not current_user.is_authenticated():
            return jsonify(**{'authenticated': False}), 401
        return func(*args, **kwargs)

    return decorated

def current_user_props():
    return {'username': current_user.username, 
        'id': current_user.id,
        'email': current_user.email,
    } if current_user.is_authenticated() else {}

def hash_password(pw):
    return pw

def check_password(pw, hashed):
    return pw == hashed



class SessionAuthAPI(MethodView):
    def post(self):
        errors = None

        request_data = request.get_json(force=True, silent=True)
        if request_data is None:
            return jsonify(**{'success': False}), 401

        if ('username' in request_data) and ('password' in request_data):
            user = User.query.filter_by(username=request_data['username']).first()

            if user and user.password == request_data['password']:
                login_user(user)

                return jsonify(**{'success': True, 'authenticated': current_user.is_authenticated(), 'user': current_user_props()})

            errors = ['Invalid username or password']

        return jsonify(**{'success': False, 'authenticated': current_user.is_authenticated(), 'errors': errors}), 401

    @session_auth_required
    def get(self):
        return jsonify(**{'authenticated': True, 'user': current_user_props()})

    def delete(self):
        logout_user()
        return jsonify(**{'success': True, 'authenticated': current_user.is_authenticated()})

session_auth_view = SessionAuthAPI.as_view('session_auth_api')
app.add_url_rule('/api/session_auth', view_func=session_auth_view, methods=['GET', 'POST', 'DELETE'])