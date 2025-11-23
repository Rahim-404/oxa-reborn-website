from typing import Dict
from flask import Flask, Blueprint, current_app, redirect, render_template, request, url_for, send_from_directory
from flask.typing import ResponseReturnValue


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__,static_folder='build',static_url_path='')

    @app.route('/')
    def index():
        return send_from_directory('build', 'index.html')

    @app.errorhandler(404)
    def not_found(e):
        return app.send_static_file('index.html')

    @app.route('/<path:path>')
    def serve_static(path):
        if os.path.isfile(os.path.join('build', path)):
            return send_from_directory('build', path)
        return send_from_directory('build', 'index.html')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0",debug=False)
