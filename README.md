# Share Code Plus

Extension de Share Code : meta données, log utilisateurs, SQL, coloration de code

## Téléchargez et installez le code de base

Placez vous dans un venv actif (onglet "Terminal" de PyCharm ou n'importe
quel terminal système où vous avez activé un venv déjà créé par ailleurs).
~~~~
git clone https://github.com/UlysseARNAUD-IPSSI/python-projet-sharecode-plus.git sharecode-plus
cd sharecode-plus
pip install -r requirements.txt
export FLASK_ENV=development
python -m flask run
# ou `python app.py` pour lancer la version BDD (pour la persistance des données)
# ou `python app-file.py` pour lancer la version fichier (pour la persistance des données)
~~~~

Allez sur http://localhost:5000/ via un navigateur internet de votre choix.


# Atelier : améliorer l'application

Livrables : dans un dépôt GIT public (gitlab, github, framagit, ...) 

- Une documentation succinte mais claire au format _markdown_ (comme ce fichier)
- Scripts et modules Python modifiés et créés
- Gabarits HTML/CSS/JS 
- Les requètes SQL de création de tables (fichier `initdb.sql`)

## Partie 1 : enregistrer le langage de programmation utilisé

Enoncé :
> Ajouter une liste déroulante dans la page Web de création/modification d'un
bout de code pour choisir le langage de programmation utilisé parmi (par
exemple) : Python, C, PHP, JavaScript, etc. Le champ sera préselectionné
avec le langage précédemment enregistré si possible.
>
> Enregistrez cette information lors de l'enregistrement du code dans un
fichier qui reprend l'id du code avec l'extension .lang (par example
si le code est dans `data/wMdWMbwAQ` on pourra trouver "Python" dans
`data/wMdWMbwAQ.lang`

Pour cette partie, l'objet code est sérialisé (transformer en chaîne de caractères) dans un fichier dont le nom correspond à son identifiant.

La classe Code a comme variables d'instance `uid`, `content`, et `language`.

Si des soucis sont encourrus sur la branche `master`, vous pouvez utiliser la branche `partie1` via la commande suivante :
```bash
git checkout partie1
```

## Partie 2 : Changez le procédé de stockage, plus de fichiers mais un SGBDR

Enoncé :
> Copiez `sharecode.py` sous le nom `sharecodedb.py` pour cette partie et la
suite.
> 
> Note : utilisez sqlite comme SGBDR (le connecteur est disponible en standard
avec Python 3, vous n'avez qu'à installer le client sqlite en ligne de commande
pour créer le schéma de la base). En production sur un vrai serveur Web
public on utiliserait plutôt PostgreSQL ou MariaDB/MySQL.
> 
> Concevez le schéma d'une base de données, constitué d'une seule table qui
stocke les extraits de code et le langage utilisé. Les vues de l'application
seront inchangées (hors appels aux fonctions métiers), seules les fonctions
ou classes du modèle métiers seront différentes.
> 
> Nommez le module qui implémente le modèle métier utilisant sqlite sous le
nom `model_sqlite.py` en vous inspirant du modèle `model.py`.

Un fichier `model_sqlite.py` a été créé afin d'utiliser sqlite au lieu des fichiers pour la persistance des données, dont les méthodes étaient définis dans le fichier `model.py`.

## Partie 3 : enregistrez les infos sur les utilisateurs qui publient du code

Enoncé :
> Ajoutez à la base une table pour enregistrer des informations sur les utilisateurs
qui publient du code (pas les lecteurs) : adresse ip, navigateur _(user agent)_,
date et heure de dernière modification.
> 
> Ajoutez dans le modèle métier l'enregistrement de ces informations (disponibles
à travers l'objet request construit par Flask).
> 
> Ajoutez une page accessible à travers /admin qui montre les extraits de code
publiés et ces informations concernant la dernière modification.


Une table `logs` a été créée dont les valeurs contenues sont `uid`, `address_ip` et `user_agent`.

Les valeurs `updated_at` et `created_at` sont utilisées dans les tables afin d'avoir la possibilité de loguer les entrées de la base de données.

L'affichage ne fonctionne pas mais on peut s'attendre à recevoir les valeurs sur la page http://localhost:5000/admin.

## Partie 4 : colorisation de code

Enoncé :
> Il existe un module Python pour colorer syntaxiquement du code : pygment.
> 
> Installez ce module, mettez à jour requirements.txt, utilisez le pour colorer
le code affiché par la page associée aux URLs de type `/view/.../` dans le bon
langage (celui enregistré en base de données).

Pygments n'a pas été pris en compte. A la place, une librairie JS a été utilisé qui est CodeMirror.

Je n'ai pas réussi à implémenter la coloritation syntaxique (malgré un début de système dont on récupère le mime en fonction du langage), cependant en utilisant la librarie CodeMirror, nous pouvons ajouté des addons comme la recherche de mot (comme dans un ide) dans l'éditeur de code.

**EDIT : Vendredi 24 juillet à 18h : La coloritation syntaxique fonctionne et un nombre conséquent de langages sont disponibles dans la selection des langages.**

## Partie optionnelle

Enoncé :
> - Pourrait-on détecter automatiquement le langage utilisé ? Comment ?
> - Améliorez l'esthétique du site et son confort d'utilisation (grace à
  vos connaissance d'HTML 5, CSS et JavaScript). Le site doit pouvoir
  néanmoins être utilisable si JS est désactivé côté navigateur !
> - Ajoutez une _black list_ des IP d'utilisateur en base, administrable
  par l'administrateur du site (ne vous occupez pas de l'authentification
  sur les pages d'admin, on peut configurer cela côté serveur Web de
  production -- Apache, NGINX, ...). Un utilisateur dont l'IP est dans
  cette liste se voit interdire l'accès en écriture au site.
> - Développez un ensemble de vues pour accéder aux services de partage
  de code via une API REST sur des URLs de la forme : `/api/...`.
  Documentez cette API et fournissez un script (Python ou Shell) de
  test de l'API.


