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
    user = ""
    uo = user_by_id(current_user.userID)
    if uo is not None:
        user = uo.read()  # placed in list for easier/consistent use within HTML

    notes = []
    for note in uo.notes:
        note = note.read()  # convert to JSON
        note['note'] = markdown.markdown(note['note'])  # markdown to html
        notes.append(note)

    return render_template('notes.html', user=user, notes=notes)


# Preserve redirect after login to go to intended next page
next_page = None
