from flask import send_from_directory

import os

from .. import app



STATIC_PATH = app.config['STATIC_PATH']



@app.route('/js/<path:path>')
def serve_js(path):
    return serve_static_path('js', path)

@app.route('/css/<path:path>')
def serve_js(path):
    return serve_static_path('css', path)

@app.route('/img/<path:path>')
def serve_js(path):
    return serve_static_path('img', path)

@app.route('/templates/<path:path>')
def serve_templates(path):
    return serve_static_path('templates', path)



def serve_static_path(directory, path):
    print STATIC_PATH
    return send_from_directory(STATIC_PATH, os.path.join(directory, path).replace('\\','/'))
