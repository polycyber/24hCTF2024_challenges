# Sur les traces de Scofield 2

## Write-up FR

Il faut commencer par retrouver la marque de ces bâtonnets au fromage.
2 façons parmi d'autres:
- Une recherche avec Google Image nous permet de trouver ce [groupe Facebook](https://www.facebook.com/groups/149535758996361/) de fans de Cheezies.
- Comme on demande un identifiant [TC LID](https://fr.wikipedia.org/wiki/Indicateur_d%27emplacement#Indicateur_de_Transports_Canada), on cherche un aérodrome canadien. Sur [Wikipedia](https://en.wikipedia.org/wiki/Cheese_puffs#Notable_brands) on trouve la liste des plus importantes marques de bâtonnets au fromage et une seule est canadienne c'est Cheezies.
 
Une fois qu'on a trouvé [la marque](https://en.wikipedia.org/wiki/Cheezies), on découvre que la production se fait dans la ville de Belleville, Ontario et que [l'inventeur des Cheezies](https://en.wikipedia.org/wiki/James_Marker) y a fondé [un aérodrome](https://en.wikipedia.org/wiki/Belleville_Aerodrome).
L'identifiant de cet aérodrome est **CNU4**. On calcule son hash MD5 ce qui nous donne le flag.

## Write-up EN

You have to start by finding the brand of these cheese sticks.
2 ways among others:
- A search with Google Image allows us to find this [group Facebook](https://www.facebook.com/groups/149535758996361/) of Cheezies fans.
- Since we are asking for an identifier [TC LID](https://fr.wikipedia.org/wiki/Indicateur_d%27emplacement#Indicateur_de_Transports_Canada), we are looking for a Canadian aerodrome. On [Wikipedia](https://en.wikipedia.org/wiki/Cheese_puffs#Notable_brands) we find the list of the most important brands of cheese sticks and only one is Canadian, Cheezies.

Once we found [the brand](https://en.wikipedia.org/wiki/Cheezies), we discovered that production was done in the town of Belleville, Ontario and that [the inventor of Cheezies](https://en.wikipedia.org/wiki/James_Marker) founded [an aerodrome](https://en.wikipedia.org/wiki/Belleville_Aerodrome) there. The identifier of this aerodrome is **CNU4**. We calculate its MD5 hash which gives us the flag.

## Flag

`polycyber{c28c51c8b2f9c2ddbf331a3e56e664be}`
