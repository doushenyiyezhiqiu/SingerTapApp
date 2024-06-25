import requests
from flask import Flask, request, redirect, url_for
import os

app = Flask(__name__)

app_key = os.getenv("APP_KEY")
app_secret = os.getenv("APP_SECRET")
redirect_uri = "http://localhost:5000/callback"
scope = ""

@app.route('/')
def home():
    auth_url = f"https://www.tiktok.com/auth/authorize?response_type=code&client_key={app_key}&redirect_uri={redirect_uri}&scope={scope}"
    return redirect(auth_url)

@app.route('/callback')
def callback():
    code = request.args.get('code')
    token_url = "https://open-api.tiktok.com/oauth/access_token/"
    params = {
        "client_key": app_key,
        "client_secret": app_secret,
        "code": code,
        "grant_type": "authorization_code"
    }

    response = requests.post(token_url, data=params)
    access_token = response.json().get("access_token")
    return f"Access Token: {access_token}"

if __name__ == '__main__':
    app.run(debug=True)
