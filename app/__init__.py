from flask import Flask

#initialize flask application ando also register Blueprint

def create_app():
    #get an object from flask framework
    app = Flask(__name__)
    #import and register the blueprint in routes file
    from .routes import main
    app.register_blueprint(main)

    return app