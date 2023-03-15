from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    locale = db.Column(db.String(20))
    models = db.relationship('Modelm', back_populates='author', cascade='all')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amp_name = db.Column(db.Text)
    amp_model = db.Column(db.Text)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='items')
