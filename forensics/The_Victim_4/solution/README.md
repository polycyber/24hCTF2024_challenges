# The Victim 4

## Write-up FR

Le principe du dernier défi est de simplement cracker le mot de passe d'une archive zip à l'aide d'une attaque par dictionnaire. La liste de mot de passe est fournie lors de la complétion du défi 3.
1. Convertir le zip en un format crackable pour john avec: zip2john Dylan_Perry.zip > zip.hash
2. Le fichier venait avec un liste de mot de passe, un simple: john --wordlist=list.txt zip.hash devrait être suffisant pour trouver le mot de passe
3. Le flag se trouve directement dans l'archive Dylan_Perry.zip

## Write-up EN

The principle of the last challenge is simply to crack the password of a zip archive using a dictionary attack. The password list is provided when completing challenge 3.

Convert the zip file into a format crackable by John with: zip2john Dylan_Perry.zip > zip.hash
Since the file comes with a password list, a simple: john --wordlist=list.txt zip.hash should be sufficient to find the password.
The flag is directly inside the Dylan_Perry.zip archive.

## Flag

`polycyber{4ccE$s_To_d47a_Gr4NT3D}`
