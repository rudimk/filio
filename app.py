from flask import Flask, redirect
from flask.ext.basicauth import BasicAuth
from creds import username, password

app = Flask(__name__)

app.debug = True
app.config['BASIC_AUTH_USERNAME'] = username
app.config['BASIC_AUTH_PASSWORD'] = password

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def secret_view():
    return redirect('/admin')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9200)