from flask import request, jsonify
from flask.views import MethodView
from flask.ext.login import current_user

from server.models.food import FoodEntry
from server.api.sessionauth import session_auth_required

from server import app, db, login_manager



class MenuAPI(MethodView):
    def get(self):
        menu_items = FoodEntry.query.filter_by(active=True).all()

        item_list = []

        for item in menu_items:
            obj = {
                'name': item.name,
                'active': item.active,
                'price': item.price,
                'restaurant': item.restaurant.name,
                'imageurl_icon': item.imageurl_icon,
                'imageurl_full': item.imageurl_full,
            }

            obj['tags'] = [tag.name for tag in item.tags]

            item_list.append(obj)

        response_json = {'items': item_list}

        return jsonify(**response_json)

menu_view = MenuAPI.as_view('menu_api')
app.add_url_rule('/api/menu', view_func=menu_view, methods=['GET'])