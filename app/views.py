from app import app
from flask import flash, redirect, url_for, session, request, render_template
from .drchrono_api import api as drchrono_api


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',
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

    flash("Logged in successfully!")
    return redirect(url_for('account'))


@app.route('/account')
def account():
    user = drchrono_api.get_current_user(session["access_token"])
    return render_template('account.html', user=user)


@app.route('/offices')
def offices():
    offices = drchrono_api.get_offices(session["access_token"])
    return render_template('offices.html', offices=offices)


@app.route('/appointments')
@app.route('/appointments/<int:office_id>')
def appointments(office_id=None):
    office = None
    if office_id is not None:
        office = drchrono_api.get_office_info(session["access_token"],
                                              office_id)

    appointments = drchrono_api.get_appointments(session["access_token"],
                                                 office_id)
    return render_template('appointments.html', office=office,
                           appointments=appointments)
