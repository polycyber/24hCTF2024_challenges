# Ungoing Cafeteria Development

## Write-up FR

*Le fichier .apk final a été passé dans un obfuscateur et n'est pas dispo dans ce repo*

Il y a deux façons principales de le résoudre.

La première est de décompiler le apk et chercher dans le code les classes "custom". DrawingView.kt montre différentes actions DrawRect avec des coordonnées.
Un reverse engineer motivé peut se faire un petit script qui parse les coordonnées et qui reproduit le dessin sur un plan cartésien pour dessiner le flag, ou encore exécuter le code dans un autre contexte.

La deuxième façon est la façon prévue:
1- Constater la présence d'une activité Admin dans le AndroidManifest.xml
2- Installer l'application
3- Connecter adb 
3.1 - adb devices
3.2 - adb shell
4- Une fois dans le téléphone, on peut déclencher l'activité non protégée directement en ligne de commande pour accéder à l'interface d'administration
5 - # am start -n com.example.cafeteriaapp/.AdminActivity
6- La page admin s'ouvre sur l'application et révèle le flag dessiné avec des rectangles.

NOTE: Android version 29 ou moins doit être utilisé. Ceci est indiqué par la description et pourrait forcer le participant à installer un émulateur avec Android Studio qui cible la bonne version. Il s'agit alors d'une étape de plus à prendre en compte.


## Write-up EN

*The final .apk file has gone through an obfuscator and is not present in this repo*

There are two main ways of solving this problem.

The first is to decompile the apk and search the code for custom classes. DrawingView.kt shows various DrawRect actions with coordinates.
A motivated reverse engineer can create a small script that parses the coordinates and reproduces the drawing on a Cartesian plane to draw the flag, or execute the code in another context.

The second way is the intended way:
1- Check for the presence of an Admin activity in the AndroidManifest.xml file.
2- Install the application
3- Connect adb 
3.1 - adb devices
3.2 - adb shell
4- Once on the phone, you can trigger the unprotected activity directly from the command line to access the administrative interface
5 - # am start -n com.example.cafeteriaapp/.AdminActivity
6- The admin page opens on the application and reveals the flag drawn with rectangles.

NOTE: Android version 29 and under must be used. This is hinted by the challenge description and may force the participant to install an emulator with Android Studio, having the required version.


## Flag

`polycyber{3HH7}`
