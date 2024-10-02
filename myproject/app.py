from flask import Flask, render_template
from config import Config
from extensions import db
from flask_migrate import Migrate
from routers import main

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    register_resources(app)
    register_extensions(app)
    return app

def register_extensions(app):
    db.init_app(app)
    migrate = Migrate(app,db)

def register_resources(app):
    @app.route('/home')
    def home():
        print("Rendering index.html")  
        return """<html
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Flask App</title>
</head>
<body>
    <h1>Welcome to My Flask App</h1>
    <p>This is a basic HTML page.</p>
</body>
</html>"""


def register_resources(app):

    app.register_blueprint(main)

if __name__ == '__main__':
    app = create_app()
    print("Starting Flask app...")  
    app.run('127.0.0.1', 5000)