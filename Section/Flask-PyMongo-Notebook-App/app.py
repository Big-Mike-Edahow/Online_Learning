# app.py
# Flask-PyMongo Notes app

from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://localhost:27017/flaskCrashCourse"
mongo = PyMongo(app)

@app.route("/")
def home():
    # Get the notes from the database
    notes = list(mongo.db.notes.find({}));

    return render_template("home.html",homeIsActive=True,addNoteIsActive=False,notes=notes)

@app.route("/add-note", methods=['GET','POST'])
def addNote():
    if(request.method == "GET"):

        return render_template("add-note.html",homeIsActive=False,addNoteIsActive=True)

    elif (request.method == "POST"):

        # get the fields data
        title = request.form['title']
        description = request.form['description']

        # save the record to the database
        mongo.db.notes.insert_one({"title":title,"description":description})

        # redirect to home page
        return redirect("/")

@app.route('/edit-note', methods=['GET','POST'])
def editNote():

    if request.method == "GET":

        # get the id of the note to edit
        noteId = request.args.get('form')


        # get the note details from the db
        note = dict(mongo.db.notes.find_one({"_id":ObjectId(noteId)}))

        # direct to edit note page
        return render_template('edit-note.html',note=note)

    elif request.method == "POST":

        #get the data of the note
        noteId = request.form['_id']
        title = request.form['title']
        description = request.form['description']

        # update the data in the db
        mongo.db.notes.update_one({"_id":ObjectId(noteId)},{"$set":{"title":title,"description":description}})

        # redirect to home page
        return redirect("/")

@app.route('/delete-note', methods=['POST'])
def deleteNote():

    # get the id of the note to delete
    noteId = request.form['_id']

    # delete from the database
    mongo.db.notes.delete_one({ "_id": ObjectId(noteId)})

    # redirect to home page
    return redirect("/")

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(debug=True)

# sudo systemctl start mongod.service
# sudo systemctl status mongod

