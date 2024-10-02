from extensions import db

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)  # Corregido 'Interger' a 'Integer'
    name = db.Column(db.String(80), nullable=False, unique=True)
    email = db.Column(db.String(200), nullable=False, unique=True)
    password = db.Column(db.String(100))
    created_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now())  # Corregido 'server_defaul' a 'server_default'
    update_at = db.Column(db.DateTime(), nullable=False, server_default=db.func.now(), onupdate=db.func.now())  # Igual aquí

    @property
    def data(self):
        return {
            'id': self.id,
            'username': self.name,
            'email': self.email,
            'password': self.password
        }

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        r = cls.query.all()
        result = []

        for i in r:
            result.append(i.data)
        return result
    @classmethod
    def get_by_id(cls,id):
        return cls.query.filter(cls.id == id).first()
    