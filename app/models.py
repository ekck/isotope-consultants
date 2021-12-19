# app/models.py
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login_manager

class User(UserMixin, db.Model):
    """
    Create a Users table
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(60), index=True, unique=True)
    username = db.Column(db.String(60), index=True, unique=True)
    first_name = db.Column(db.String(60), index=True)
    last_name = db.Column(db.String(60), index=True)
    password_hash = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        """
        Prevent password from being accessed
        """
        raise AttributeError('password is not a readable attribute.')

    @password.setter
    def password(self, password):
        """
        Set password to a hashed password
        """
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User: {}>'.format(self.username)
    


# Set up user_loader
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Role(db.Model):
    """
    Create a Role table
    """

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), unique=True)
    description = db.Column(db.String(200))
    users = db.relationship('User', backref='role',
                                lazy='dynamic')

    def __repr__(self):
        return '<Role: {}>'.format(self.name)

class Isotope(db.Model):
    """
    Create Isotope table
    """

    __tablename__ = 'isotope'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    location = db.Column(db.String(50))
    physical_location = db.Column(db.String(50))
    box_number = db.Column(db.Integer)
    town = db.Column(db.String(50))
    number = db.Column(db.Integer)
    email = db.Column(db.String(50))
    objective = db.Column(db.String(200))
    vision = db.Column(db.String(200))
    mission = db.Column(db.String(200))

    def __repr__(self):
        return '<Isotope: {}>'.format(self.name)

class Service(db.Model):
    """
    Create Service table
    """

    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50)) 
    description = db.Column(db.String(200))

    def __repr__(self):
        return '<Service: {}>'.format(self.name)

class Staff(db.Model):
    """
    Create Staff table
    """

    __tablename__ = 'staffs'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    position = db.Column(db.String(50))
    qualification = db.Column(db.String(50))
    

    def __repr__(self):
        return '<Staff: {}>'.format(self.name)

class Article(db.Model):
    """
    Create an Articles table
    """

    __tablename__ = 'articles'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    author = db.Column(db.String(50))
    date = db.Column(db.DateTime, default=datetime.utcnow)
    body = db.Column(db.Text)
    tags = db.Column(db.String(50))
    draft = db.Column(db.Boolean, default=False)
    

    def __repr__(self):
        return '<Blog: {}>'.format(self.title)

class Cartegory(db.Model):
    """
    Create Cartegory table
    """

    __tablename__ = 'cartegories'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    description = db.Column(db.String(200))
    

    def __repr__(self):
        return '<Carteory: {}>'.format(self.name)



    