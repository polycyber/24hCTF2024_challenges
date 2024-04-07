# The Victim 3

## Write-up FR

Puisque l'on sait que l'on cherche des infos sur Dylan Perry. La description du défi parle aussi de la pointe de l'iceberg. Il s'avère que dans le dossier Public/Pictures contiennent plusieurs photos d'iceberg.

Les images sont toutes nommées par deux lettres séparée d'un trait de soulignement. Puisque l'on cherche des informations sur Dylan Perry, et qu'une des images est nommées d_p.png, il est possible de venir à la conclusion que c'est la bonne image à analyser. Elle est aussi plus grosse que les autres images présentes dans le dossier.

Avec un outil comme OpenStego, il est possible d'extraire un fichier zip de l'image. En décompressant le zip, on obtient 3 fichier: le flag, le fichier list.txt et une deuxième archive nommée Dylan_Perry.zip.

## Write-up EN

Since we know that we are looking for information about Dylan Perry, and the challenge description also mentions the tip of the iceberg, it turns out that the Public/Pictures folder contains several photos of icebergs.

The images are all named with two letters separated by an underscore. Since we are seeking information about Dylan Perry, and one of the images is named d_p.png, it is possible to conclude that this is the correct image to analyze. It is also larger than the other images in the folder.

Using a tool like OpenStego, it is possible to extract a zip file from the image. By decompressing the zip, you get three files: the flag, the file list.txt, and a second archive named Dylan_Perry.zip

## Flag

`polycyber{One_mORE_5TEp_BeFOrE_Th3_eNd}`
