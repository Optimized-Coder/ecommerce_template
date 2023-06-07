from ..extensions import db
from flask_login import UserMixin
from werkzeug.security import check_password_hash, generate_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, default='admin')
    password = db.Column(db.Text)

    def __repr__(self):
        return '<User %r>' % self.username
    
    def check_password(self, input_password):
        return check_password_hash(self.password, input_password)
    
    def set_password(self, password):
        self.password = generate_password_hash(password)
        db.session.commit()
        return self.password