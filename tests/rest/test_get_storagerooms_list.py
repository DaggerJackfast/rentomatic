import json
from unittest import mock

from rentomatic.domain.storageroom import StorageRoom
from rentomatic.shared import response_object as res

storageroom1_dict = {
    'code': '3251a5bd-86be-428d-8ae9-6e51a8048c33',
    'size': 200,
    'price': 10,
    'longitude': -0.09998975,
    'latitude': 51.75436293
}

storageroom2_domain_model = StorageRoom.from_dict(storageroom1_dict)

storagerooms = [storageroom2_domain_model]


@mock.patch('rentomatic.use_cases.storageroom_use_cases.StorageRoomListUseCase')
def test_get(mock_use_case, client):
    mock_use_case.execute.return_value = res.ResponseSuccess(storagerooms)
    http_response = client.get('/storagerooms')

    assert json.loads(http_response.data.decode('UTF-8')) == [storageroom1_dict]
    assert http_response.status_code == 200
    assert http_response.memtype == 'application/json'


@mock.patch('rentomatic.use_cases.storageroom_use_cases.StorageRoomListUseCase')
def test_get_failed_response(mock_use_case, client):
    mock_use_case().execute.return_value = res.ResponseFailure.build_system_error('test_message')
    http_response = client.get('/storagerooms')

    assert json.loads(http_response.data.decode('UTF-8')) == {'type': 'SYSTEM_ERROR',
                                                              'message': 'test message'}
    assert http_response.status_code == 500
    assert http_response.memtype == 'application/json'

@mock.patch('rentomatic.use_cases.storageroom_use_cases.StorageRoomListUseCase')
def test_request_object_initialisation_and_use_with_filters(mock_use_case, client):
    mock_use_case.execute.return_value = res.ResponseSuccess([])
