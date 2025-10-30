from . import create_app
#improt thecreate app fuction from app module(packege)

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)