#!/usr/bin/env python3

"""
Importation des modules
"""

from flask import Flask, request, render_template, \
    redirect, jsonify

from model_sqlite import createTables, \
    createCode, \
    getCode, \
    getAllCode, \
    updateCode, \
    createEdition, \
    getEdition

"""
Initialisation
"""

app = Flask(__name__)
createTables()

languages = [
    'text',
    'python',
    'html',
    'css',
    'javascript'
]



"""
Page d'accueil
"""

@app.route('/')
def index():
    return render_template('index.html')



"""
Création d'un code
"""

@app.route('/create')
def create():
    uid = createCode() # Créer la ligne
    return redirect("{}edit/{}".format(request.host_url,uid)) # Ne fait pas de redirection mais affiche la page


"""
Modification d'un code
"""

@app.route('/edit/<string:uid>/', methods=['GET'])
def edit(uid):
    code = getCode(uid)
    if code is None:
        return render_template('error.html', uid=uid)
    d = dict(uid=uid, code=code, languages=languages,
             url=f"{request.host_url}view/{uid}")
    return render_template('edit.html', **d)


"""
Publication d'un code
"""

@app.route('/publish', methods=['POST'])
def publish():
    content = request.form.get('content')
    uid = request.form.get('uid')
    language = request.form.get('language')

    # code = Code(uid=uid, content=content, language=language)

    updateCode(uid, content, language)
    return jsonify({'ok': True})

"""
Affichage d'un code
"""

@app.route('/view/<string:uid>/')
def view(uid):
    code = getCode(uid)

    if code is None:
        return render_template('error.html', uid=uid)

    d = dict(uid=uid, code=code, languages=languages,
             url=f"{request.host_url}view/{uid}")

    return render_template('view.html', **d)

"""
Administration
"""

@app.route('/admin/')
def admin():
    pass


"""
Vue partielle : Derniers codes modifiées
"""

@app.route('/_partials/last-added')
def partialsLastAdded():
    d = {'last_added': getAllCode()}
    return render_template('/partials/last-added.html', **d)


"""
Execution de l'application
"""

if __name__ == '__main__':
    app.run()
