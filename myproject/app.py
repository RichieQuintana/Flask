from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usuarios.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Modelo de Usuario
class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)

# Crear base de datos dentro de un contexto de aplicación
with app.app_context():
    db.create_all()

# Ruta principal (CRUD)
@app.route('/')
def index():
    usuarios = Usuario.query.all()
    return render_template('index.html', usuarios=usuarios)

# Ruta para crear nuevos usuarios
@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        username = request.form['username']
        nuevo_usuario = Usuario(username=username)
        db.session.add(nuevo_usuario)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('create.html')

# Ruta para actualizar un usuario
@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    usuario = Usuario.query.get(id)
    if request.method == 'POST':
        usuario.username = request.form['username']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', usuario=usuario)

# Ruta para eliminar un usuario
@app.route('/delete/<int:id>')
def delete(id):
    usuario = Usuario.query.get(id)
    if usuario:
        db.session.delete(usuario)
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
