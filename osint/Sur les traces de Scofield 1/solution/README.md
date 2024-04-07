# Sur les traces de Scofield 1

## Write-up FR

Il faut commencer par trouver de quelle prison s'est enfuis Michael Scofield. Après une [rapide recherche](https://fr.wikipedia.org/wiki/Prisons_de_Prison_Break#P%C3%A9nitencier_d'%C3%89tat_de_Fox_River_(Fox_River_State_Penitentiary)), on apprend que c'est l'ancienne prison de Joliet qui a servi de lieu de tournage pour la prison de Fox River.
Maintenant, on va chercher l'aérodrome de la ville de Joliet et on trouve [ce site](https://jolietpark.org/joliet-regional-airport). On trouve dans l'onglet "Pilot Services" l'identifiant FAA de l'aérodrome : **JOT**. On calcule son hash MD5 ce qui nous donne le flag.

## Write-up EN

We need to start by finding out which prison Michael Scofield escaped from. After a [quick search](https://en.wikipedia.org/wiki/Prison_Break#Filming), we learned that it was the former Joliet prison that served as a filming location for Fox River Prison.
Now we go look for the city of Joliet airfield and we find [this site](https://jolietpark.org/joliet-regional-airport). In the “Pilot Services” tab you can find the FAA identifier of the aerodrome: **JOT**. We calculate its MD5 hash which gives us the flag.

## Flag

`polycyber{88be398c2d0a9c6fccbeb28b020c3226}`
