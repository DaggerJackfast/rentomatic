import falcon
from rentomatic.rest.storageroom import StorageRoom
from rentomatic.rest.index import Index

# TODO : add auth and csrf middleware

index = Index()
storagerooms = StorageRoom()


def create_app():
    app = falcon.API()

    app.add_route('/', index)
    app.add_route('/storagerooms', storagerooms)
    return app
