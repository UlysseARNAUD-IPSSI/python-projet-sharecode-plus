#!/usr/bin/env python3

"""
Importation des modules
"""

from flask import Flask, request, render_template, \
    redirect, jsonify

from Code import Code
from model_sqlite import createTables, \
    createCode, \
    getCode, \
    getAllCode, \
    updateCode, \
    createLog, \
    getLog

"""
Initialisation
"""

app = Flask(__name__)
createTables()

languages = {
    'APL',
    'PGP',
    'Asn.1',
    'Brainfuck',
    'Clike',
    'Clojure',
    'CMake',
    'Cobol',
    'Coffeescript',
    'Commonlisp',
    'Crystal',
    'CSS',
    'Cypher',
    'D',
    'Dart',
    'Diff',
    'Django',
    'Dockerfile',
    'DTD',
    'Dylan',
    'EBNF',
    'ECL',
    'Eiffel',
    'Elm',
    'Elm',
    'Erlang',
    'Factor',
    'FCL',
    'Forth',
    'Fortran',
    'Gas',
    'GFM',
    'Gherkin',
    'Go',
    'Groovy',
    'HAML',
    'Handlebars',
    'Haskell',
    'Haxe',
    'HTML',
    'HTTP',
    'IDL',
    'Javascript',
    'Jinja2',
    'Julia',
    'Livescript',
    'Lua',
    'Markdown',
    'Mathematica',
    'Modelica',
    'Nginx',
    'NSIS',
    'Octave',
    'Oz',
    'Pascal',
    'Perl',
    'PHP',
    'Pig',
    'Powershell',
    'Properties',
    'Protobuf',
    'Pug',
    'Puppet',
    'Plain text',
    'Python',
    'Q',
    'R',
    'RPM',
    'Ruby',
    'Rust',
    'SAS',
    'SASS',
    'Scheme',
    'Shell',
    'Sieve',
    'Slim',
    'Smalltalk',
    'Smarty',
    'Spreadsheet',
    'SQL',
    'Stylus',
    'Swift',
    'TCL',
    'Textile',
    'Tiddlywiki',
    'Tiki',
    'TOML',
    'Tornado',
    'Turtle',
    'Twig',
    'VB',
    'VBScript',
    'Velocity',
    'Verilog',
    'VHDL',
    'Vue',
    'XML',
    'YAML',
    'Yacas',
    'Z80'
}

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
    uid = createCode()
    createLog(request.remote_addr, request.user_agent.string)
    return redirect(f'{request.host_url}edit/{uid}')


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
    content = request.form['content']
    uid = request.form['uid']
    language = request.form['language']

    updateCode(uid, content, language)
    createLog(request.remote_addr, request.user_agent.string)
    result = getCode(uid)

    return jsonify({'ok': True, 'code': result})


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
    d = dict(editions=getLog())
    return render_template('admin.html', **d)


"""
Vue partielle : Derniers codes modifiées
"""


@app.route('/_partials/last-added')
def partialsLastAdded():
    d = {'last_added': getAllCode(), 'languages': languages}
    return render_template('/partials/last-added.html', **d)


"""
Execution de l'application
"""

if __name__ == '__main__':
    app.run()
