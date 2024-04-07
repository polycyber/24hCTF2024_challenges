# The Victim 2

## Write-up FR

On sait que le directeur de la prison aiment bien les photos de prisons. S'il l'on va dans le dossier Pictures de l'utilisateur director, il est possible de voir qu'il est plein de photos de prisons. Il risque d'avoir des problèmes de permissions pour accéder au contenu du dossier. Pour régler ce problème, il faut ouvrir le disque en mode "Write temporary" puis changer les permissions du dossier dans le disque monté.

En exécutant exiftool sur toutes les photos de prison extraites du disque, puis en faisant un grep sur le polycyber, il est alors possible de trouver le flag. (Il est possible d'exécuter exiftool sur le contenu d'un dossier avec l'option -r).

## Write-up EN

We know that the prison director enjoys prison photos. If we go to the Pictures folder of the director's user, it is possible to see that it is full of prison photos. There may be permission issues while trying to access the folder's content. To resolve this issue, it is necessary to open the disk in 'Write temporary' mode and then change the permissions of the folder on the mounted disk.

By running exiftool on all the prison photos extracted from the disk, and then using grep for "polycyber," it is then possible to find the flag. (It is possible to run exiftool on the contents of a folder with the -r option).

## Flag

`polycyber{Dylan_Perry}`
