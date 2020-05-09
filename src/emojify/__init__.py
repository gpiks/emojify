"""Server for emojifying """
__version__ = "0.1"

import os

from flask import Flask
from flask import abort
from flask import request

from .text_processor import remove_stop_words


def create_app(test_config=None):
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # a default secret that should be overridden by instance config
        SECRET_KEY="dev",
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile("config.py", silent=True)
    else:
        # load the test config if passed in
        app.config.update(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route("/", methods=["GET", "POST"])
    def process_text():
        if request.method == "GET":
            return "Successful test!"
        try:
            text = request.get_json()["text"]
        except KeyError:
            abort(400)
        return str(remove_stop_words(text))

    return app
