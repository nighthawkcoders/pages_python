from flask import render_template, redirect, request, url_for, send_from_directory
from flask_login import login_required

from __init__ import app, login_manager
from cruddy.app_crud import app_crud
from uploady.app_upload import app_upload
from cruddy.app_crud_api import app_crud_api
from notey.app_notes import app_notes

from cruddy.login import login, logout, authorize

app.register_blueprint(app_upload)
app.register_blueprint(app_crud)
app.register_blueprint(app_crud_api)
app.register_blueprint(app_notes)


@app.route('/')
def index():
    return render_template("index.html")


# Flask-Login directs unauthorised users to this unauthorized_handler
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    app.config['NEXT_PAGE'] = request.endpoint
    return redirect(url_for('main_login'))


# if login url, show phones table only
@app.route('/login/', methods=["GET", "POST"])
def main_login():
    # obtains form inputs and fulfills login requirements
    if request.form:
        email = request.form.get("email")
        password = request.form.get("password")
        if login(email, password):
            try:  # try to redirect to next page
                next_page = app.config['NEXT_PAGE']
                app.config['NEXT_PAGE'] = None
                return redirect(url_for(next_page))
            except:  # any failure goes to home page
                return redirect(url_for('index'))

    # if not logged in, show the login page
    return render_template("login.html")


# if login url, show phones table only
@app.route('/logout/', methods=["GET", "POST"])
@login_required
def main_logout():
    logout()
    return redirect(url_for('index'))


# user authorize with password validation
@app.route('/authorize/', methods=["GET", "POST"])
def main_authorize():
    error_msg = ""
    # check form inputs and creates user
    if request.form:
        # validation should be in HTML
        user_name = request.form.get("user_name")
        email = request.form.get("email")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")  # password should be verified
        if password1 == password2:
            if authorize(user_name, email, password1):
                return redirect(url_for('main_login'))
        else:
            error_msg = "Passwords do not match"
    # show the auth user page if the above fails for some reason
    return render_template("authorize.html", error_msg=error_msg)


# serve uploaded files so they can be downloaded by users.
@app.route('/uploads/<name>')
def uploads_endpoint(name):
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)


# register "uploads_endpoint" endpoint so url_for will find all uploaded files
app.add_url_rule(
    "/" + app.config['UPLOAD_FOLDER'] + "/<name>", endpoint="uploads_endpoint", build_only=True
)


# 404 error page redirect
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


if __name__ == "__main__":
    # Replit required port, works on IntelliJ
    app.run(host='0.0.0.0', debug=True, port=8080)
