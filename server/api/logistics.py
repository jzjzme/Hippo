from flask import request, jsonify
from flask.views import MethodView
from flask.ext.login import current_user

from server.models.users import User
from server.models.logistics import Address, CreditCard
from server.api.sessionauth import session_auth_required

from server import app, db, login_manager



class AddressAPI(MethodView):
    @session_auth_required
    def get(self):
        obj = {
            'line_1': current_user.address.line_1,
            'line_2': current_user.address.line_2,
            'city': current_user.address.city,
            'state': current_user.address.state,
            'zipcode': current_user.address.zipcode,
        } if current_user.address else None

        response_json = {'address': obj}

        return jsonify(**response_json)

    @session_auth_required
    def post(self):
        errors = None

        request_data = request.get_json(force=True, silent=True)
        if request_data is None:
            return jsonify(**{'success': False}), 401

        fields = ['line_1', 'line_2', 'city', 'state', 'zipcode']

        for field in fields:
            if field not in request_data:
                return jsonify(**{'success': False}), 401

        current_user.address = Address(**dict((field, request_data[field]) for field in fields))

        db.session.add(current_user)
        db.session.commit()

        return jsonify(**{'success': True})

address_view = AddressAPI.as_view('address_api')
app.add_url_rule('/api/user/address', view_func=address_view, methods=['GET', 'POST'])



class CreditCardAPI(MethodView):
    @session_auth_required
    def get(self):
        obj = {
            'credit_card_number': current_user.creditcard.credit_card_number,
            'expiration_month': current_user.creditcard.expiration_month,
            'expiration_year': current_user.creditcard.expiration_year,
            'security_code': current_user.creditcard.security_code,
        } if current_user.creditcard else None

        response_json = {'creditcard': obj}

        return jsonify(**response_json)

    @session_auth_required
    def post(self):
        errors = None

        request_data = request.get_json(force=True, silent=True)
        if request_data is None:
            return jsonify(**{'success': False}), 401

        fields = ['credit_card_number', 'expiration_month', 'expiration_year', 'security_code']

        for field in fields:
            if field not in request_data:
                return jsonify(**{'success': False}), 401

        current_user.creditcard = CreditCard(**dict((field, request_data[field]) for field in fields))

        db.session.add(current_user)
        db.session.commit()

        return jsonify(**{'success': True})

creditcard_view = CreditCardAPI.as_view('creditcard_api')
app.add_url_rule('/api/user/creditcard', view_func=creditcard_view, methods=['GET', 'POST'])