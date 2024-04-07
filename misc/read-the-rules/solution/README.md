# Nom du défi

## Write-up FR

Si on lit réellement les règles, on remarque que l'avant-avant dernière ligne des règles explique comment former le flag:

`Il est obligatoire de placer “rules” dans les accolades du format proposé plus bas pour valider le premier défi.`

Le format proposé plus bas est `^polycyber{.+}$`, donc on obtient polycyber{rules}.

## Write-up EN

If one actually reads the rules, it is noticed that the second-to-last line of the rules explains how to form the flag:

"It is mandatory to place 'rules' inside the curly braces of the format proposed below to validate the first challenge."

The proposed format below is ^polycyber{.+}$, so the result is polycyber{rules}.

## Flag

`polycyber{rules}` ou `polycyber{"rules"}`
