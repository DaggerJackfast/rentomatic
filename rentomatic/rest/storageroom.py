import json
import falcon
from rentomatic.use_cases import request_objects as req
from rentomatic.shared import response_object as res
from rentomatic.repository import memrepo as mr
from rentomatic.use_cases import storageroom_use_cases as uc
from rentomatic.serializers import storageroom_serializer as ser

STATUS_CODES = {
    res.ResponseSuccess.SUCCESS: falcon.HTTP_200,
    res.ResponseFailure.RESOURCE_ERROR: falcon.HTTP_404,
    res.ResponseFailure.PARAMETERS_ERROR: falcon.HTTP_400,
    res.ResponseFailure.SYSTEM_ERROR: falcon.HTTP_500,
}
first_storageroom = {
    'code': 'f853578c-fc0f-4e65-81b8-566c5dffa35a',
    'size': 215,
    'price': 39,
    'longitude': '-0.09998975',
    'latitude': '51.75436293',
}

second_storageroom = {
    'code': 'fe2c3195-aeff-487a-a08f-e0bdc0ec6e9a',
    'size': 405,
    'price': 66,
    'longitude': '0.18228006',
    'latitude': '51.74640997',
}

third_storageroom = {
    'code': '913694c6-435a-4366-ba0d-da5334a611b2',
    'size': 56,
    'price': 60,
    'longitude': '0.27891577',
    'latitude': '51.45994069',
}


class StorageRoom(object):

    def on_get(self, request, response):
        qrystr_params = {
            'filters': {},
        }
        for arg, values in request.params.items():
            if arg.startswith('filter_'):
                qrystr_params['filters'][arg.replace('filter_', '')] = values

        request_object = req.StorageRoomListRequestObject.from_dict(qrystr_params)
        repo = mr.MemRepo([
            first_storageroom,
            second_storageroom,
            third_storageroom,
        ])
        use_case = uc.StorageRoomListUseCase(repo)
        response_result = use_case.execute(request_object)

        response.body = json.dumps(response_result.value, cls=ser.StorageRoomEncoder)
        response.set_header('mimetype', 'application/json')
        response.set_header('Powered-By', 'Falcon')
        response.status = STATUS_CODES[response_result.type]
