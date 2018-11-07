from tempfile import mkdtemp

from flask import Flask

from flask_tus.views import FlaskTus


def create_app():
    app = Flask(__name__)
    app.config.update({
        'TESTING': True,
        'UPLOAD_DIR': mkdtemp(),
        'UPLOAD_VIEW': '/files/',
        'TUS_MAX_SIZE': 2 ** 32  # 4 gigabytes
    })

    flask_tus = FlaskTus(app)
    flask_tus.init_app(app)

    return app
