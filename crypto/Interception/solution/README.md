# Interception

## Write-up FR

Voici deux solutions de résoudre le défi.

Tout d'abord, il est possible de placer le hash dans un fichier `hash.txt` et d'utiliser hashcat avec le dictionnaire rockyou.txt pour retrouver le mot de passe avec la commande suivante: `hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt`. L'option `-m` permet d'indiquer à hashcat que le hash fourni est de type NTLM.

Une autre façon est d'utiliser des solutions en ligne qui ont déjà calculer le hash, comme le site [hashes.com](https://hashes.com) par exemple.

## Write-up EN

Here are two solutions to solve the challenge.

Firstly, you can place the hash in a file `hash.txt` and use hashcat with the rockyou.txt dictionary to find the password with the following command: `hashcat -m 1000 hash.txt /usr/share/wordlists/rockyou.txt`. The `-m` option specifies to hashcat that the provided hash is of type NTLM.

Another way is to use online solutions that have already calculated the hash, such as the website [hashes.com](https://hashes.com), for example.

## Flags

`polycyber{michikitolindo}`
