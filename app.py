#!/usr/bin/env python3

from flask import Flask, request, render_template, \
    redirect, jsonify

from model import save_doc_as_file, \
    read_doc_as_file, \
    get_last_entries_from_files

import Code

app = Flask(__name__)


@app.route('/')
def index():
    # d = { 'last_added':[ { 'uid':'testuid', 'code':'testcode' } ] }
    return render_template('index.html')


@app.route('/create')
def create():
    uid = save_doc_as_file()
    return redirect(f"{request.host_url}edit/{uid}")


@app.route('/edit/<string:uid>/', methods=['GET'])
def edit(uid):
    code = read_doc_as_file(uid)
    if code is None:
        return render_template('error.html', uid=uid)
    d = dict(uid=uid, code=code,
             url=f"{request.host_url}view/{uid}")
    return render_template('edit.html', **d)


@app.route('/publish', methods=['POST'])
def publish():
    code = request.form.get('code')
    uid = request.form.get('uid')
    language = request.form.get('language')

    save_doc_as_file(uid, code)
    return jsonify({
        'ok': True
    })


@app.route('/view/<string:uid>/')
def view(uid):
    code = read_doc_as_file(uid)
    if code is None:
        return render_template('error.html', uid=uid)
    d = dict(uid=uid, code=code,
             url="{}view/{}".format(request.host_url, uid))
    return render_template('view.html', **d)


@app.route('/admin/')
def admin():
    pass


@app.route('/_partials/last-added')
def partialsLastAdded():
    d = {'last_added': get_last_entries_from_files()}
    return render_template('/partials/last-added.html', **d)


if __name__ == '__main__':
    app.run()
