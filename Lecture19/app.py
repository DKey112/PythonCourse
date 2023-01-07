from flask_app.app1.views import app1
from flask import Flask



def create_app():
    app = Flask(__name__, template_folder='template')
    app.config.from_object('config.DevelopmentConfig')
    app.register_blueprint(app1)
    return app


if __name__ == "__main__":
    create_app().run(debug= True)