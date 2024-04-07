# Doorman

## Write-up FR

### Étudier le protocole

Pour commencer, vous devez d'abord ouvrir le fichier `.pcap` dans Wireshark pour analyser les données envoyées entre le client et le serveur. Nous pouvons voir une conversation entre 172.17.0.1 (semblant être un client) et 172.17.0.2 (semblant être un serveur) sur le port 8998.

Tout d'abord, l'utilisateur est accueilli avec un message TCP contenant: `\x00\x16\x12\x14KEY:c6131e45816ac6e6` (24 octets). Immédiatement après, le client répond.

Cela signifie que le client a compris que le message du serveur était probablement terminé. Si nous regardons le début du message, nous pouvons voir `\x00\x16`. Puisque `0x16 == 0x0016 == 22`, nous pouvons raisonnablement supposer que les deux premiers octets représentent la taille du message sans l'en-tête de 2 octets.

Pour récapituler, chaque message que nous envoyons devrait ressembler à (pseudocode):

```c
struct message {
    u16_t msg_len;
    u8_t msg[msg_len];
};
```

Le premier message a maintenant une séquence d'octets inconnue `\x12\x14`.
Le deuxième octet peut avoir son utilisation déduite puisque `\x14 == 20`, qui est la longueur du texte brut `KEY:...` après. Cependant, `\x12` semble inconnu.

Le deuxième message envoyé ressemble à: (sans l'en-tête de 2 octets)

```none
\x12\x16\x0a\x05admin\x12\x08\xb6rm6\xf6\x05\xb4\x82\x1a\x03198
```

À partir de cela, nous pouvons également voir beaucoup d'octets `\x12`. En effectuant des recherches en ligne avec des requêtes telles que "protocoles avec octet \x12", nous pouvons voir quelques résultats mentionnant protobuf.

Sur un éditeur en ligne tel que [Cyberchef](https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)From_Hex('Auto')Protobuf_Decode('',false,true)&input=MTIxNDRiNDU1OTNhNjMzNjEzMzMxNjUzNDM1MzgzMTM2NjE2MzU2CjEyMTYwYTA1NjE2NDZkNjk2ZTEyMDhiNjcyNmQzNmY2MDViNDgyMWEwMzMxMzkzOA==), nous pouvons voir que les deux messages semblent être des messages Protobuf valides.

En analysant les types affichés sur Cyberchef, nous pouvons construire un protobuf de base pour les messages reçus:

```protobuf
message ResponseKey {
    string msg = 2;
}

message RequestLogin {
    string username = 1;
    string password = 2;
    string otp = 3;
}

message ActualMessage {
    RequestLogin login = 2;
}
```

### Premier flag

Maintenant que nous savons que le serveur utilise Protobuf, nous pouvons essayer d'obtenir le premier flag.

Nous pouvons essayer de simuler une connexion, à travers la même requête envoyée par l'utilisateur, cependant, nous sommes informés que nos identifiants ne correspondent pas.

Cela signifie que le mot de passe est probablement chiffré, ce qui nécessiterait une clé, que le serveur nous a gentiment envoyée au début.

En effectuant un simple XOR avec [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'c6131e45816ac6e6'%7D,'Standard',false)&input=YjYgNzIgNmQgMzYgZjYgMDUgYjQgODI), nous pouvons voir que le mot de passe est ... `password`.

Ensuite vient le `otp`. Cependant, en expérimentant avec celui-ci, nous pouvons voir qu'il s'agit du premier octet de la clé.

Avec cela, nous pouvons construire un message de connexion valide.

Après nous être connectés, nous pouvons décoder le premier message envoyé par le client:

```protobuf
message RequestDoor {
    int32 id = 1;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
}
```

Notez que protobuf attribue par défaut des valeurs vides à 0 (la plupart du temps).

Nous pouvons ensuite essayer de forcer d'autres champs, comme le champ = 2 dans la requête, et nous pouvons voir que la porte s'ouvre et nous obtenons le flag.

Cela se produit parce que le champ = 2 est `false` par défaut, ce qui signifie de ne pas ouvrir la porte.

### Deuxième flag

Pour le deuxième flag, nous pouvons regarder le deuxième message envoyé.

Selon CyberChef, la requête ressemble à quelque chose comme:

```json
{
    "1": 2,
    "4": {
        "1": "log_0.txt",
        "2": 0
    }
}
```

Maintenant, si nous construisons sur ce que nous savions auparavant, cela pourrait être simplifié à:

```protobuf
message RequestWithFileName {
    string fileName = 1;
    int32 something = 2;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
    RequestWithFileName file = 4;
}
```

La sortie du serveur après cette demande semble être le contenu du fichier. Cependant, en essayant de faire une traversée de chemin ou autre chose à la place de `log_0.txt`, cela semble ne pas fonctionner, le serveur répondant que les fichiers ne sont pas accessibles.

Cependant, en changeant la valeur du deuxième champ (`something`) à 1, nous pouvons voir une liste de répertoire, montrant le fichier `flag.txt`.

Maintenant, en essayant de lire le contenu de ce fichier révèle notre deuxième flag.

### Troisième flag

Le flag précédent a révélé un fichier nommé `flag_admin.txt`, cependant, essayer d'y accéder ne semble pas fonctionner. Si nous regardons la prochaine demande émise dans le pcap, nous pouvons voir qu'elle ressemble à quelque chose comme cela:

```json
{
    "1": 3,
    "5": {
        "1": "Subject 2217429 has exited his cell",
        "2": "cams.24hctf"
    }
}
```

De plus, lors de la réception de la demande, le serveur effectue une demande à 172.17.0.3, qui est probablement l'adresse résolue de `cams.24hctf`.

Si nous essayons de réassembler cela en langage protobuf réel, nous pouvons essayer de déduire que cela ressemble à ceci:

```protobuf
message RequestWithHost {
    string data = 1;
    string dnsName = 2;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
    RequestWithFileName file = 4;
    RequestWithHost host = 5;
}
```

En essayant l'hôte où se trouve le défi, le serveur répond avec `"\000\026\022\024KEY:90488afdc37624e0\000 \010\001\022\034Invalid password or username"`. Cela semble très familier, et le serveur nous envoie essentiellement la sortie de sa requête.
drapeau
Maintenant, nous avons un SSRF :). Il est temps de l'exploiter. Ce qui est amusant, c'est que les serveurs ont généralement confiance en localhost, et donc cela pourrait nous mener à lire le `flag_admin.txt` précédent.

Le problème est que essayer `localhost` et `127.0.0.1` ne fonctionne pas. Cela nous donne quelques erreurs:

- `Pas de localhost !!!`
- `Le nom d'hôte ne correspond pas à Regex: ^[0-9A-Za-z\.]+\.[A-Za-z]+$`

Un truc amusant que nous pouvons essayer est de coder différemment l'adresse IP, cependant cela échouerait également car l'expression régulière attend à ce que la fin soit une chaîne de caractères.

Le serveur attend essentiellement n'importe quel nom DNS valide, tant qu'il ne contient pas la chaîne `localhost` et se termine par une chaîne alphabétique (pour le TLD).

Cette protection peut cependant être contournée, car le DNS est un service tiers, faisant correspondre des noms à des adresses IP. Qui dit qu'il ne pourrait pas y avoir un nom qui se résout en 127.0.0.1?

La recherche en ligne de services qui redirigent vers des adresses IP personnalisées semble nous amener vers des services comme <https://sslip.io/> et <https://nip.io/>.

En utilisant l'un de ces services avec localhost, nous pouvons contourner l'authentification et obtenir le `flag_admin.txt`.



## Write-up EN

### Reversing the protocol

To get started, you must first open the `.pcap` file in Wireshark to analyze the data being sent between the client and server.
We can see a conversation between 172.17.0.1 (seems like a client) and 172.17.0.2 (seems like a server) on port 8998.

Firstly, the user is greeted with a TCP message with the contents: `\x00\x16\x12\x14KEY:c6131e45816ac6e6` (24 bytes). Immediately after, the client responds.

This means that the client understood the server's message was probably over. If we look at the beginning of the message, we can see `\x00\x16`.
Since `0x16 == 0x0016 == 22`, we can safely assume that the first two bytes represent the size of the message without the 2 byte header.

So to recap, each message we send should look like (pseudocode):

```c
struct message {
    u16_t msg_len;
    u8_t msg[msg_len];
};
```

The first message now has an unknown `\x12\x14` byte sequence.
The second byte can have its use deduced since `\x14 == 20` which is the length of the plaintext `KEY:...` after. However, `\x12` seems unknown.

The second message sent looks like: (without 2 byte header)

```none
\x12\x16\x0a\x05admin\x12\x08\xb6rm6\xf6\x05\xb4\x82\x1a\x03198
```

From this, we can also see a lot of `\x12` bytes. By looking online with queries like "protocols with \x12 byte", we can see a few results mentioning protobuf.

On an online editor such as [Cyberchef](https://gchq.github.io/CyberChef/#recipe=Fork('%5C%5Cn','%5C%5Cn',false)From_Hex('Auto')Protobuf_Decode('',false,true)&input=MTIxNDRiNDU1OTNhNjMzNjMxMzMzMTY1MzQzNTM4MzEzNjYxNjMzNjY1MzYKMTIxNjBhMDU2MTY0NmQ2OTZlMTIwOGI2NzI2ZDM2ZjYwNWI0ODIxYTAzMzEzOTM4), we can see that both messages seem to be valid Protobuf messages.

By analyzing the types shown on Cyberchef, we can construct a basic protobuf for received messages:

```protobuf
message ResponseKey {
    string msg = 2;
}

message RequestLogin {
    string username = 1;
    string password = 2;
    string otp = 3;
}

message ActualMessage {
    RequestLogin login = 2;
}
```

### First flag

Now that we know the server deals in Protobuf, we can try and get the first flag.

We can try to simulate a login, through the same request sent by the user, however, we are notified that our credentials do not match.

This means the password is probably encrypted, which would call for a key, which the server has kindly sent to us at first.

By performing a simple XOR with [Cyberchef](https://gchq.github.io/CyberChef/#recipe=From_Hex('Auto')XOR(%7B'option':'Hex','string':'c6131e45816ac6e6'%7D,'Standard',false)&input=YjYgNzIgNmQgMzYgZjYgMDUgYjQgODI), we can see that the password is ... `password`.

Next is the `otp`. However, by experimenting with it, we can see it is the first byte of the key.

With this, we can construct a valid login message.

After we are logged in, we can decode the first message sent by the client:

```protobuf
message RequestDoor {
    int32 id = 1;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
}
```

Note that protobuf defaults its empty values to 0 (most of the time).

We can then try to brute force other fields, like the field = 2 in the request, and we can see that the door opens and we get the flag.

This happens because the field = 2 is `false` by default, meaning to not open the door.

### Second flag

For the second flag, we can look at the second message being sent.

According to CyberChef, the request looks something like:

```json
{
    "1": 2,
    "4": {
        "1": "log_0.txt",
        "2": 0
    }
}
```

Now if we build on top of what we knew before, it could be simplified to:

```protobuf
message RequestWithFileName {
    string fileName = 1;
    int32 something = 2;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
    RequestWithFileName file = 4;
}
```

The output from the server after this request seems to be the file's content. However, by trying to do a path traversal or anything else instead of `log_0.txt` seems to not work, with the server answering that the files are not accessible.

However, by changing the value of the second field (`something`), to 1, we can see a directory listing, showing the file `flag.txt`.

Now trying to read this file's contents reveals our second flag.

### Third flag

The previous flag revealed a file named `flag_admin.txt`, however, trying to access it does not seem to work. If we look at the next request issued in the pcap, we can see it looks something like this:

```json
{
    "1": 3,
    "5": {
        "1": "Subject 2217429 has exited his cell",
        "2": "cams.24hctf"
    }
}
```

Furthermore, upon receiving the request, the server makes a request to 172.17.0.3, which is probably the resolved address of `cams.24hctf`.

If we try to reassemble this into actual protobuf language, we can try to deduce it looks like this:

```protobuf
message RequestWithHost {
    string data = 1;
    string dnsName = 2;
}

message ActualMessage {
    int32 id = 1;
    RequestLogin login = 2;
    RequestDoor door = 3;
    RequestWithFileName file = 4;
    RequestWithHost host = 5;
}
```

Trying the host where the challenge is hosted, the server replies with `"\000\026\022\024KEY:90488afdc37624e0\000 \010\001\022\034Invalid password or username"`. This seems awfully familiar, and the server is basically sending us the output from its request.

We now have an SSRF :). Time to exploit it. What's fun about this is that servers usually trust localhost, and so it could lead our way to reading the `flag_admin.txt` from before.

The issue is trying `localhost` and `127.0.0.1` does not work. It gives us a few errors:

- `No localhost!!!`
- `Hostname does not match Regex: ^[0-9A-Za-z\.]+\.[A-Za-z]+$`

A funky trick we can try is encoding the IP address differently, however this would also fail as the regex expects the ending to be a string.

The server is basically expecting any valid DNS name, as long as it does not contain the string `localhost` and ends with an alphabetical string (for the TLD).

This protection though can be bypassed, as DNS is a third party service, mapping names to IP addresses. Who says there couldn't be a name that resolves to 127.0.0.1?

Searching online for services that redirect to custom IPs seems to bring us to services like <https://sslip.io/> and <https://nip.io/>.

By using one of these with localhost, we can bypass the authentication and get the `flag_admin.txt`.

## Flags

1. `polycyber{pR0t0b00f_15_c0oL_RiGh7?}`
2. `polycyber{i_W0nd_er_wh47s_nXt}`
3. `polycyber{inc3pt_10n_937hnfuy3t7dt35}`
