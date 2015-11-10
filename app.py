from flask import Flask, redirect
from flask.ext.basicauth import BasicAuth
from creds import username, password
from flask_admin import Admin
from flask_admin.contrib.fileadmin import FileAdmin
import os.path as op

# Flask setup here
app = Flask(__name__)
admin = Admin(app, name='Filio', template_mode='bootstrap3')

path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))

app.config['BASIC_AUTH_USERNAME'] = username
app.config['BASIC_AUTH_PASSWORD'] = password
app.config['BASIC_AUTH_FORCE'] = True

basic_auth = BasicAuth(app)

@app.route('/')
@basic_auth.required
def secret_view():
    return redirect('/admin')


if __name__ == '__main__':
	app.run(host='0.0.0.0', port=9500, debug=True)