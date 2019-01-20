#models.py -- all the database stuff goes here
import os
import pymysql
import configparser
from flask import Flask
#from forms import AddForm, DelForm -- may not need this yet // will be password protected
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))
config = configparser.ConfigParser()
config.read('.db.cnf')
db_user = config['db']['user']
db_pw = config['db']['password']

#Can remove this as I will be importing models
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://{}:{}@localhost/tutorial_db'.format(db_user,db_pw)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app) # This step will essentially finish up setting our sqlite database
Migrate(app,db) # Flask Migrate essentially connects our app with the existing database that we create above

### CLASS DEFINITIONS AKA SCHEMA

class Anecdotes(db.Model):

    __tablename__ = 'anecdotes'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)

    def __init__(self,title):
        self.title = title

    def __repr__(self):
        return f"ID: {self.id}, Anecdote Title: {self.title}"

############
