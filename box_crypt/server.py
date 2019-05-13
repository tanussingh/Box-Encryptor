from flask import Flask, redirect, request, render_template, send_from_directory
from boxsdk import Client
from boxsdk import OAuth2
from uiFunctions import *

# Start the flask app
app = Flask(__name__)

class Auth:
    client_id = 'rmuj8eqddadgw1ohpyvlonfy4zl6zfyt'
    client_secret = 'DtzvPtLlm4Nto68Lv5xQXnGiHy1fcV5V'
    redirect_uri = 'http://127.0.0.1:5000/auth'

    oauth = OAuth2(
        client_id=client_id,
        client_secret=client_secret
    )

    auth_url, csrf_token = oauth.get_authorization_url(redirect_uri)

    auth_code = None

    access_token = None
    refresh_token = None

    client = None


@app.route('/', methods=['GET'])
def index():
    if Auth.client is None:
        return redirect('/login')

    return redirect('/home')


@app.route('/login', methods=['GET'])
def login():
    return redirect(Auth.auth_url)


@app.route('/auth', methods=['GET'])
def auth():
    # TODO: What if CSRF check fails
    assert request.args['state'] == Auth.csrf_token

    Auth.auth_code = request.args['code']
    Auth.access_token, Auth.refresh_token = Auth.oauth.authenticate(
        Auth.auth_code)

    Auth.client = Client(Auth.oauth)

    return redirect('/register')

@app.route('/register', methods=['GET'])
def register():
    from register import start
    start(Auth.client)

    return redirect('/home')

@app.route('/home', methods=['GET'])
def hello():

    return render_template('hello.html')


@app.route('/share', methods=['GET', 'POST'])
def share():
    if Auth.client is None:
        return redirect('/login')

    if request.method == 'POST':
        uiShare(Auth.client, request.form['Collaborator'], request.form['Filename'])
        return redirect("/home")

    return render_template("share.html")


@app.route('/view', methods=['GET', 'POST'])
def view():
    if Auth.client is None:
        return redirect('/login')

    #get list of files for ui and uiView
    fileinfos = boxSearch(Auth.client)

    if request.method == 'POST':
        uiView(Auth.client, request.form['Sharer'], request.form['Filename'], fileinfos)
        return redirect("/home")
    
    names=[]
    for x in fileinfos:
        if (".bc" in x.name):
            names.append(x.name.replace(".bc", ""))

    return render_template("view.html", names=names)


@app.route('/img/<path:path>')
def send_img(path):
    return send_from_directory('templates/img', path)


def main():
    app.run(debug=True)


main()
