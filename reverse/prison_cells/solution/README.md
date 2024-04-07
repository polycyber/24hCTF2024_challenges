# Nom du défi

## Write-up FR

Ce défi peut être résolu de quelques façons différentes.

Tout d'abord, on remarque que l'on a la possibilité d'ouvrir les cellules de prison, mais rien d'intéressant ne s'en suit. En désassemblant/décompilant le programme avec un outil comme Ghidra, on observe qu'une option "flag" est aussi disponible. C'est la trace qu'on utilisé les précédents criminels qui ont aidé à faire sortir leur ami Davey de la prison. Un problème se pose toutefois: le programme demande de prouver qu'on est bien Davey.

On peut comprendre que le programme contacte une url, mais celle-ci est décryptée dynamiquement. Cette fonction de décryption semble assez difficile à comprendre. L'oeil aguerri saura le reconnaitre, mais il est aussi possible de le présenter à un LLM comme ChatGPT, qui saura l'identifier. Lorsqu'on sait que l'encryption est RC4, il est possible de récupérer le texte chiffré (premier paramètre) ainsi que la clé (troisième paramètre). Il est possible que Ghidra laisse la clé sous le format hexadécimal. Il suffit alors de retyper la variable à char[4] pour qu'on voit plus clairement que la valeur est plutôt "flag". Lorsqu'on utilise ensuite CyberChef avec la recette (1) From Hex et (2) RC4 (avec "flag" comme clé) on obtient alors la valeur décryptée: get_flag_328cd65f3ec16a7c64bebdd90d2e2b3c (voici la valeur encryptée pour convenance: 0x8895a056ad8a2a57e56ae76013ebde5bafa34306e00cc7df481b06ab733ba5cf5b81f19441b59a8e62)

On peut voir que la suite du programme consiste simplement à concaténer l'adresse du serveur à la chaine de caractères que l'on vient d'obtenir. On peut alors simplement contacter le serveur et récupérer le flag avec un programme comme curl!

Il aurait aussi été possible de rouler le programme dans un débuggeur puis récupérer la route HTTP décryptée, mais il y avait une petite protection pour l'empêcher. En effet, une fonction (qui était appelée à quelques endroits dans le programme) terminait l'exécution du programme lorsque gdb était détectée. Pour contourner cela, il était possible d'utiliser un autre débuggeur ou modifier le binaire pour contourner la fonction d'anti-debug.

Lorsque exécuté, le programme demande aussi de vérifier que nous sommes bien Davey. Pour lui faire croire que c'est le cas, il faut entrer le mot de passe qui est encrypté dans le programme avec un simple XOR utilisant 0x09 comme clé. En appliquant plutôt un xor sur la clé encrypté, on obtient XUQWeHDQaCbBZZcQ, qui correspond bien au mot de passe. On peut découvrir ces informations en analysant la seconde fonction appelée dans celle qui s'occupe de la connexion internet (celle qui utilise les fonctions curl_easy_init, curl_easy_setopt, etc).

Il était aussi possible de laisser le programme contacter le serveur et récupérer le flag, mais celui-ci n'est alors pas affiché car il est directement stocké en mémoire. Pour trouver cette adresse, il suffit de consulter la fonction de connexion internet, récupérer la fonction de callback qui traite la valeur de retour du serveur (fournie au second appel à curl_easy_setopt) et récupérer l'adresse mémoire. Ceci aurait permis de récupérer le flag si on souhaitait exécuter tout le programme dans un débuggeur.

Finalement, une autre méthode aurait été de rouler le programme normalement, rentrer la valeur demandée, puis récupérer la réponse du serveur avec l'aide d'un sniffeur réseau comme Wireshark.

## Flag

`polycyber{GU4RD5_CH4NG3_SH1F7_47_M1DN1GH7}`

## Write-up EN

This challenge can be solved in a few different ways.

Firstly, it is noticed that there is the option to open the prison cells, but nothing interesting follows from it. By disassembling/decompiling the program using a tool like Ghidra, one observes that a "flag" option is also available. This is the trace used by previous criminals who helped their friend Davey escape from prison. However, a problem arises: the program requires proof that one is indeed Davey.

It is understood that the program contacts a URL, but it is decrypted dynamically. This decryption function seems quite challenging to understand. An experienced eye may recognize it, or it can be presented to a Language Model like ChatGPT, which can identify it. Knowing that the encryption is RC4, it is possible to retrieve the encrypted text (first parameter) and the key (third parameter). Ghidra might leave the key in hexadecimal format. Simply retyping the variable to char[4] makes it clear that the value is "flag." Using CyberChef with the recipe (1) From Hex and (2) RC4 (with "flag" as the key), the decrypted value is obtained: get_flag_328cd65f3ec16a7c64bebdd90d2e2b3c (here is the encrypted value for convenience: 0x8895a056ad8a2a57e56ae76013ebde5bafa34306e00cc7df481b06ab733ba5cf5b81f19441b59a8e62).

The next step in the program is to concatenate the server address to the string obtained. Then, one can simply contact the server and retrieve the flag using a program like curl!

It would have also been possible to run the program in a debugger and retrieve the decrypted HTTP route, but there was a small protection to prevent it. A function (called at various points in the program) terminated the program when GDB was detected. To circumvent this, another debugger could be used, or the binary could be modified to bypass the anti-debug function.

When executed, the program also asks to verify that one is indeed Davey. To make it believe so, the password encrypted in the program with a simple XOR using 0x09 as the key should be entered. Applying XOR to the encrypted key, XUQWeHDQaCbBZZcQ is obtained, which corresponds to the password. These details can be discovered by analyzing the second function called within the one handling internet connection (the one using functions like curl_easy_init, curl_easy_setopt, etc).

It was also possible to let the program contact the server and retrieve the flag, but it was not displayed as it was directly stored in memory. To find this address, inspect the internet connection function, retrieve the callback function processing the server's return value (provided in the second call to curl_easy_setopt), and obtain the memory address. This would have allowed retrieving the flag if one wanted to execute the entire program in a debugger.

Finally, another method would have been to run the program normally, enter the requested value, and then retrieve the server's response with the help of a network sniffer like Wireshark.

## Flag

`polycyber{GU4RD5_CH4NG3_SH1F7_47_M1DN1GH7}`
