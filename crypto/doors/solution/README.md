# Prison Doors

## Write-up FR

Pour la première partie, les participants doivent se connecter en tant qu'invité. Cela leur donne un cookie contenant un JWT. Ensuite, ils doivent décoder le JWT à l'aide d'un outil tel que [celui-ci](https://jwt.io).
Le JWT contient un champ appelé flag qui contient le premier flag.  

Pour la deuxième partie, le participant doit effectuer une attaque par force brute sur la clé utilisée pour générer le JWT. Cela peut être fait via John The Ripper:
`john jwt.txt --wordlist=rockyou.txt`  

La clé de signature est `gyarados500`. Une fois de plus, en utilisant jwt.io, le participant peut saisir la clé de signature et modifier le jeton pour
définir `is_admin` sur true, puis visiter la page /admin.html pour obtenir le flag.

## Write-up EN

For the first part, the participants needs to login as a guest. That gives them a cookie containing a JWT. They then need to decode the JWT using a tool like [this one](https://jwt.io).
The JWT contains a field named `flag` that contains the first flag.

For the second part, the participant needs to bruteforce the key used to generate the jwt. This can be done via John The Ripper:
`john jwt.txt --wordlist=rockyou.txt`

The signing key is `gyarados500`. Once again using [jwt.io](https://jwt.io), the participant can input the signing key and modify the token to set `is_admin` to `true` and then visit the `/admin.html` page to get the flag.

## Flags

`polycyber{JwtAreN0t3ncrypt3d}`
`polycyber{WhyW0uldYouUseAPa$$wordAsAKey?}`