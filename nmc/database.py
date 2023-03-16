from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, index=True)
    password_hash = db.Column(db.String(128))
    locale = db.Column(db.String(20))
    models = db.relationship('Model', back_populates='author', cascade='all')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)


class Model(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    capture_type = db.Column(db.Text, nullable=False)
    pedal_name = db.Column(db.Text)
    amp_name = db.Column(db.Text)
    cab_name = db.Column(db.Text)
    nam_model = db.Column(db.Text, nullable=False)
    nam_model_filename = db.Column(db.Text)
    is_public = db.Column(db.Boolean, default=False)
    is_ampsim = db.Column(db.Boolean, default=False)
    likes = db.Column(db.Integer, default=0)
    created_date = db.Column(DateTime, default=func.now(), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', back_populates='items')
