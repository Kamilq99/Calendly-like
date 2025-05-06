import pytest
from flask import Flask
from controller.controller import controller

@pytest.fixture
def app():
    app = Flask(__name__)
    app.register_blueprint(controller)
    return app

@pytest.fixture
def client(app):
    return app.test_client()

def test_plan_event(client):
    data = {
        'id': 1,
        'user_name': 'Jan',
        'last_name': 'Kowal',
        'plan_name': 'Go Shopping Today',
        'email': 'test@example.com',
        'date': '2022-01-01',
        'time': '10:00'
    }
    
    response = client.post('/api/plan/new', json=data)
    
    assert response.status_code == 200
    assert response.is_json

    json_data = response.get_json()
    assert json_data['id'] == data['id']
    assert json_data['user_name'] == data['user_name']
    assert json_data['last_name'] == data['last_name']
    assert json_data['plan_name'] == data['plan_name']
    assert json_data['email'] == data['email']
    assert json_data['date'] == data['date']
    assert json_data['time'] == data['time']
