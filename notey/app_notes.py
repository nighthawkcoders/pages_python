import markdown
from flask import Blueprint, render_template
from flask_login import login_required, current_user
from cruddy.query import user_by_id

# blueprint defaults https://flask.palletsprojects.com/en/2.0.x/api/#blueprint-objects
app_notes = Blueprint('notes', __name__,
                      url_prefix='/notes',
                      template_folder='templates/notey/',
                      static_folder='static',
                      static_url_path='static')


@app_notes.route('/notes')
@login_required
def notes():
    # defaults are empty, in case user data not found
    user = ""
    notes = []

    # grab user database  object based on current login
    uo = user_by_id(current_user.userID)

    # if user object is found
    if uo is not None:
        user = uo.read()                                    # extract user record (Dictionary)
        for note in uo.notes:                               # loop through each user note
            note = note.read()                              # extract note record (Dictionary)
            note['note'] = markdown.markdown(note['note'])  # convert markdown to html
            notes.append(note)                              # prepare note list for render_template
    # render user and note data
    return render_template('notes.html', user=user, notes=notes)


# Preserve redirect after login to go to intended next page
next_page = None
