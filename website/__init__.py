from flask import Flask

#initialize flask application ando also register Blueprint

#load trained labels

def create_app():
    #get an object from flask framework
    app = Flask(__name__ , template_folder='templates', static_folder='static')
    #import and register the blueprint in routes file
    from .routes import main
    app.register_blueprint(main)
    app.config.from_pyfile('config.py')

    return app