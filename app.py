from app import create_app
#improt thecreate app fuction from app module(packege)

app = create_app()

if __name__ == 'main':
    app.run(debug=True)