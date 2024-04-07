# Les repas de la cafétéria

## Write-up FR

### Premier flag
1. Inspecter la page.
2. Trouver le flag en clair avec l'indice vers /guid en dessous.
### Deuxième flag
1. Comprendre que /guid est une liste de GUID
2. Rechercher en quoi consiste une version non sécuritaire d'un GUID, comme fortement suggéré par la description du défi. On trouve sur Google qu'il existe 5 versions d'un GUID, soit (0,1,2,3,4) et que la version 1 n'est pas sécuritaire.
3. Utiliser une expression régulière pour trouver le GUID version 1 dans la liste.
4. Soumettre ce dernier dans le formulaire de la page d'accueil pour obtenir le deuxième flag.

#### Indice
C'est surtout un cherche et trouve, plutôt qu'une vulnérabilité web à exploiter.

## Write-up EN

### First flag
1. Inspect page.
2. Find flag in plain text with hint to /guid below.
### Second flag
1. Understand that /guid is a list of GUIDs
2. Find out what a non-secure version of a GUID consists of, as strongly suggested by the challenge description. Google and you'll find that there are 5 versions of a GUID (0,1,2,3,4), and that version 1 is unsafe.
3. Use a regular expression to find the GUID version 1 in the list.
4. Submit it in the form on the home page to obtain the second flag.

#### Hint
It's more of a Hide-and-Seek, less of a real web vulnerability to exploit.

## 1st Flag

`polycyber{you_should_4lw4y5_t4k3_a_look_at_the_5ourc3_51abff21c}`

## 2nd Flag
`polycyber{in53cur3_guid_v3r51on_on3_bdf23f1a}`
