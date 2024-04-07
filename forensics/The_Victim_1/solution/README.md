# The Victim 1

## Write-up FR

Il est possible de voir que le fichier n'ouvre pas avec un lecteur de PDF. En roulant "file" sur le fichier, il est possible de voir que c'est en fait un VDI. Après avoir remis l'extension originale et à l'aide d'Arsenal Image Mounter, il est possible d'ouvrir le fichier et de consulter le système de fichier. 
Il est ensuite possible de récuperer le fichier flag.txt, puisque celui-ci est à la racine du système de fichier de la VM.

## Write-up EN

It is possible to see that the file does not open with a PDF reader. By running "file" on the file, it can be seen that it is actually a VDI. After changing back the file extension and by using Arsenal Image Mounter, it is possible to open the file and examine the file system.
It is then possible to retrieve the file flag.txt since it is at the root of the VM's file system.

## Flag

`polycyber{THe_miS5ION_R3@lLY_stARTs_HErE}`
