from app import app
from flask_oauthlib.client import OAuth
import requests
import urllib

oauth = OAuth(app)

REDIRECT_URI = app.config["LOCAL_BASE_URL"] + "/authorize"

drchrono_auth = oauth.remote_app(
    'drchrono_api',
    consumer_key=app.config["DRCHRONO_APP_ID"],
    consumer_secret=app.config["DRCHRONO_APP_SECRET"],
    access_token_url='https://drchrono.com/o/token/',
    access_token_method='GET',
    authorize_url='https://drchrono.com/o/authorize/'
)


def authenticate_uri():
    uri_pieces = ["https://drchrono.com/o/authorize/?redirect_uri=",
                  urllib.quote(REDIRECT_URI),
                  "&response_type=code&client_id=",
                  urllib.quote(app.config["DRCHRONO_APP_ID"])
                  ]
    return ''.join(uri_pieces)


def authorize(code):

    r = requests.post('https://drchrono.com/o/token/', data={
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'client_id': app.config["DRCHRONO_APP_ID"],
        'client_secret': app.config["DRCHRONO_APP_SECRET"]
    })

    response = r.json()
    access_token = response['access_token']
    refresh_token = response['refresh_token']
    expires_in = response['expires_in']

    return (access_token, refresh_token, expires_in)


def logout(access_token):

    requests.post('https://drchrono.com/o/revoke_token/', data={
        'client_id': app.config["DRCHRONO_APP_ID"],
        'client_secret': app.config["DRCHRONO_APP_SECRET"],
        'token': access_token
    })


def get_current_user(access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get("https://drchrono.com/api/users/current", headers=headers)
    return r.json()


def get_office_info(access_token, office_id):
    headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get("https://drchrono.com/api/offices/" + str(office_id),
                     headers=headers)
    return r.json()


def get_offices(access_token):
    headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get("https://drchrono.com/api/offices", headers=headers)
    return r.json()


def get_appointments(access_token, params=None):
    headers = {'Authorization': 'Bearer ' + access_token}
    r = requests.get("https://drchrono.com/api/appointments",
                     headers=headers, params=params)
    return r.json()
