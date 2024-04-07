# The Timer

## Write-up FR

Il y a probablement moyen de le faire en désobfusquant le code Dart, mais ce n'est pas l'approche préconisée.
Si on assume qu'on ne tente pas de désobfusquer le code, voici les étapes:

1- Télécharger l'application sur un téléphone Android et autoriser son installation.
2- Se configurer un setup pour voir les communications vers l'externe. L'application est déjà configurée pour accepter les certificats utilisateurs et l'inspection cleartext au besoin. Si BurpSuite ne fonctionne pas, alors PCAPdroid va fonctionner. Installer PCAPdroid sur son téléphone.
3- Lancer le compteur sur l'application (le fichier .dart nous indique que ça peut être intéressant) tout en activant une capture avec PCAPdroid.
4- Constater que des requêtes http:// sont faites vers ch0ufleur.dev avec une séquence hexadécimale.
5- Avec le code Dart, on comprend que le code hexadécimal est la valeur ajoutée à l'URL et que cette valeur est construite à l'aide d'autres fonctions du même fichier.
6- Toujours en inspectant les communications, on comprend que l'adresse URL masquée dans le fichier Dart est celle de getAdress(), soit : api.ipify.org
7- Avec de la recherche on comprend que cela permet d'obtenir l'IP publique du téléphone.
8- Ensuite il faut comprendre le XOR entre le flag et la séquence \[temps restant\]+IP+\[temps restant\]+IP+\[temps restant\]+IP+\[temps restant\]+IP.
9- On peut faire l'inverse en utilisant fromCharCode et XOR dans Cyberchef en entrant la séquence en UTF-8 dans le key de XOR. On obtient le flag.

## Write-up EN

There is probably a way to do this by deobfuscating the Dart code, but this is not the recommended approach.
If we assume that we're not trying to deobfuscate the code, here are the steps:

1- Download the application on an Android phone and authorize its installation.
2- Configure a setup to view external communications. The application is already configured to accept user certificates and cleartext inspection as required. If BurpSuite doesn't work, then PCAPdroid will. Install PCAPdroid on your phone.
3- Run the timer on the application (the .dart file indicates that this could be interesting) while activating a capture with PCAPdroid.
4- Note that http:// requests are made to ch0ufleur.dev with a hexadecimal sequence.
5- Using the Dart code, we understand that the hexadecimal code is the value added to the URL and that this value is constructed using other functions in the same file.
6- Still inspecting communications, we understand that the URL address hidden in the Dart file is that of getAdress(), i.e.: api.ipify.org
7- With a little research, we understand that this allows us to obtain the phone's public IP.
8- Next, you need to understand the XOR between the flag and the sequence \[remaining time]+IP+[remaining time]+IP+[remaining time]+IP+[remaining time]+IP.
9- You can do the opposite using fromCharCode and XOR in Cyberchef, entering the UTF-8 sequence in the XOR key. The result is the flag.

## Flag

`polycyber{x0r_and_4pk_mix}`
