from werkzeug.serving import run_simple
from rentomatic.app import create_app
# TODO: add development config

if __name__ == "__main__":
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_reloader=True, use_debugger=True)
