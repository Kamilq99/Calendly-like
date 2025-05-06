from flask import Blueprint, request, jsonify
from models.models import Plan

controller = Blueprint('controller', __name__)


@controller.route('/api/plan/new', methods=['POST'])
def plan_event():
        data = request.get_json()
        id = data.get('id')
        user_name = data.get('user_name')
        last_name = data.get('last_name')
        plan_name = data.get('plan_name')
        email = data.get('email')
        date = data.get('date')
        time = data.get('time')

        plan = Plan(id, user_name, last_name, plan_name, email, date, time)

        return jsonify(plan.plan_new_event())