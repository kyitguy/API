from app import app
from flask import flash, redirect, url_for, session, request, render_template
from functools import wraps
from .drchrono_api import api as drchrono_api
from datetime import datetime


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in session:
            flash("Please login first")
            return redirect(url_for('index'))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/')
@app.route('/index')
def index():
    user = drchrono_api.get_current_user(session["access_token"])
    if 'error' in user:
        user = None
    return render_template('index.html', user=user,
                           login_uri=drchrono_api.authenticate_uri())


@app.route('/authorize')
def authorize():

    if 'error' in request.args:
        flash("Error with login")
        return redirect(url_for('index'))

    code = request.args.get('code')

    (access_token, refresh_token, expires_in) = drchrono_api.authorize(code)

    session["access_token"] = access_token
    session["refresh_token"] = refresh_token
    session["expires_in"] = expires_in

    user = drchrono_api.get_current_user(session["access_token"])
    session["username"] = user["username"]

    flash("Logged in successfully!")
    return redirect(url_for('account'))


@app.route('/logout')
def logout():
    drchrono_api.logout(session["access_token"])
    flash("You have been logged out.")
    del(session["username"])
    return redirect(url_for('index'))


@app.route('/account')
@login_required
def account():
    user = drchrono_api.get_current_user(session["access_token"])
    return render_template('account.html', user=user)


@app.route('/offices')
@login_required
def offices():
    offices = drchrono_api.get_offices(session["access_token"])
    return render_template('offices.html', offices=offices)


@app.route('/appointments')
@login_required
def appointments():
    office_id = request.args.get('office', None)
    office = None
    if office_id is not None:
        office = drchrono_api.get_office_info(session["access_token"],
                                              office_id)

    params = dict(request.args)
    date = request.args.get('date', None)
    if date is None:
        date = datetime.now().strftime('%Y-%m-%d')
        params["date"] = date

    appointments = drchrono_api.get_appointments(session["access_token"],
                                                 params)
    return render_template('appointments.html', office=office, date=date,
                           appointments=appointments)
