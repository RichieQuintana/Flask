from flask import Flask, render_template

def create_app():
    app = Flask(__name__)
    register_resources(app)
    return app

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

if __name__ == '__main__':
    app = create_app()
    print("Starting Flask app...")  
    app.run('127.0.0.1', 5000)