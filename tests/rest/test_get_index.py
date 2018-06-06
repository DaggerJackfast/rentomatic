import json


def test_get(client):
    http_response = client.simulate_get('/')
    expected = {'status': 'success', 'message': 'Server is running...'}
    assert json.loads(http_response.content.decode('UTF-')) == expected
