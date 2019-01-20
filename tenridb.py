#tenridb.py
from flask import Flask, render_template, url_for, redirect, request, Response
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import forms
from models import app,db,Anecdotes

##########
##
# CONFIGURATIONS
##
##########

# Insert any Flask configs here
#app = Flask(__name__) # This is defined in models.py

##########

##########
##
# VIEW FUNCTIONS -- Defining my routes
##
##########

@app.route('/')
def index():
    #return what would eventually be the template for the index page
    #this page will be like the wikipedia or google search page -- type in query, returns search results on a separate page
    return render_template('tenridb-home.html')


@app.route('/anecdotes', methods=['GET','POST'])
def anecdotes():
    #What I'm going to do is I'm going to pre-load all of the anecdotes -- and then the form will filter out the searches

    return render_template('tenridb-anecdotes.html')


@app.route('/anecdotes/all', methods=['GET','POST'])
def anecdotes_all():
    anecdotes = Anecdotes.query.all()
    return render_template('tenridb-anecdotes-all.html',anecdotes=anecdotes)


@app.route('/anecdotes/<anecdote_id>')
def anecdote(anecdote_id):
    #page for an individual anecdote
    anecdote = Anecdotes.query.filter_by(id=anecdote_id).all()
    #anec_title = Anecdotes.query.with_entities(Anecdotes.title).filter_by(id=anecdote_id).all()

    return render_template('tenridb-anecdotes-specific.html',anecdote=anecdote)


@app.route('/anecdotes/add', methods=['GET','POST'])
def add_anecdote():

    return "<h1>This will be the 'Add' Form</h1>"
#
#    form = AddForm()
#
#    if form.validate_on_submit():
#        title = form.title.data
#        new_anecdote = Anecdote(title)
#        db.session.add(new_anecote)
#        db.session.commit()
#
#        return redirect(url_for('anecdotes'))
#
#    return render_template('tenridb-add-anecdote.html',form=form)


@app.route('/progress')
def progress():
    #return what would eventually be the template for Progress notes
    #this page will be return a directory listing of all the progresses -- grid view?
    return render_template('tenridb-progress.html')


#Adding a Dynamic Route for different Articles
@app.route('/anecdotes/<story_number>')
def dynamic_anecotes(story_number):
    return "<h1>This is the story number: {}</h1>".format(story_number)



if __name__ == "__main__":
    app.run(debug=True)
