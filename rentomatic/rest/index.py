import falcon
import json


class Index(object):

    def on_get(self, request, response):
        response.body = json.dumps({'status': 'success', 'message': 'Server is running...'})
        response.set_header('mimetype', 'application/json')
        response.set_header('Powered-By', 'Falcon')
        response.status = falcon.HTTP_200
