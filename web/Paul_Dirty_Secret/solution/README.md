# Nom du défi

## Write-up FR

### Etape 1 : Découverte du site

En se connectant à l'adresse donnée, on est redirigé vers "fun-in-jail.ctf". Il faut l'ajouter à notre `/etc/hosts` sur Linux (`C:\Windows\System32\drivers\etc\hosts` sur Windows). Si ça n'arrive pas directement, la redirection aura lieu à l'étape 2.

### Etape 2 : Trouver un point d'entrée

Avec un peu de fuzzing (ou de guessing), on trouve facilement 2 potentielle page : `login.php` et `admin.php`, mais la seconde nous redirige sur le login.
Avec quelques tests on peut se rendre compte qu'il y a une injection SQL sur le login

### Etape 3 : Exploiter l'injection SQL

L'injection est facilement exploitable, seulement il ne faut qu'1 seule *row* en réponse.
La payload est donc la suivante :
`' OR 1=1 LIMIT 1; -- `

On est connecté sur la page `admin.php`

### Etape 4 : Exploiter une LFI

Ici, on peut lire différents fichiers.
Seulement, en modifiant le paramètre `filename`, on peut contrôler le fichier à lire.
On peut notamment effectuer un *Path Traversal*.

En cherchant à lire le fichier *index.php*, on va remonter les dossier en utilisant `..`.
Avec `../index.php` on peut lire l'index et on a un premier flag.

`polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}`

### Etape 5 : Trouver le site secret

On nous parle d'un site secret, mais où peut-il bien être ?
En se renseignant un peu, on apprend qu'on peut définir plusieurs vhost [voir ici](https://httpd.apache.org/docs/2.4/vhosts/examples.html)

On peut trouver notamment 2 fichiers par défaut pour les configurer :
- `/etc/apache2/sites-available/000-default.conf`
- `/etc/apache2/sites-enabled/000-default.conf`


Et en allant les lire on trouve un nouveau vhost et le chemin vers ses fichiers : *secret-barbapapa-addicts.ctf*

### Etape 6 : Obtenir les données cachées

On trouve un site en l'honneur des barbapapas. Malheureusement un mot de passe/secret est demandé.
En réutilisant la vulnérabilité LFI trouvée plus tôt, on peut aller lire le fichier `/var/www/html/secret-site/index.php`.
On voit que le mot de passe que l'on donne est hashé en Sha1 et vérifié avec un secret en base de données.
On peut aussi noter la présence d'une comparaison faible :
```php
if ($row["secret"] == $password)
```


En réutilisant aussi l'injection SQL, on peut obtenir, par Boolean Based ou Time Based, la valeur de ce secret.
Le secret est le suivant : `0e39467675362791795113850062806237025205`

On voit qu'il commence par `0e` et n'est composé que de chiffre.
En exploitant ceci et la comparaison faible, on peut contourner le secret !

En allant chercher [ici](https://github.com/spaze/hashes/blob/master/sha1.md), on peut trouver une liste de "magic hash", des valeurs qui une fois hashées en Sha1 donnent `0exxxx`.
On en prend un au hasard (par exemple *aaO8zKZF*) et on l'envoie, ce qui nous donne le 2ème flag !


`polycyber{One_server_multiple_vhosts...And_use_===_please!}`


## Write-up EN

Expliquer l'approche attendue pour résoudre le défi en anglais
**TODO**

## Flag 1

`polycyber{SQLi_To_LFI_but_where_is_the_hidden_site?}`

## Flag 2
`polycyber{One_server_multiple_vhosts...And_use_===_please!}`
