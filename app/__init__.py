from flask.ext.sqlalchemy import SQLAlchemy
from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)

from app.rss_gen.views import mod as rss_module
app.register_blueprint(rss_gen_module)

#controllers
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'ico/favicon.ico')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
