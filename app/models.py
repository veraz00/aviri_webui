import os
from datetime import datetime 
from app.extensions import bootstrap, db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Admin(UserMixin, db.Model):
    __tablename__ = 'tbl_admin'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    master = db.Column(db.String(20))
    about = db.Column(db.Text)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def validate_password(self, password):
        return check_password_hash(self.password_hash, password)

