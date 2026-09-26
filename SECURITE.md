# Sécurité de la connexion — mise en place

L'application vérifie désormais les mots de passe avec **Firebase Authentication**.
Les mots de passe ne sont plus écrits dans le code ni enregistrés dans Firestore, et les
données ne sont accessibles qu'aux comptes connectés et actifs.

> **Important :** avant de mettre la nouvelle version en ligne, faites les deux réglages
> Firebase ci-dessous (étapes 1 et 2), puis mettez le fichier en ligne et créez votre compte
> tout de suite (étape 3). Les anciens identifiants ne fonctionnent plus.

## Ce qui a changé

| Avant | Maintenant |
|---|---|
| Mots de passe écrits dans le code (`admin123`, `agent123`…) | Plus aucun mot de passe dans le code |
| Liste des comptes et mots de passe en clair dans `appdata/config` | Profils dans la collection `users` (nom, rôle, actif), **sans mot de passe** |
| Mot de passe vérifié dans le navigateur (contournable) | Mot de passe vérifié par Firebase |
| Base Firestore en « mode test » (ouverte à tous) | Règles : seuls les comptes connectés et actifs accèdent aux données |
| Suppression d'un compte | Désactivation (le compte ne peut plus se connecter, l'historique reste) |
| Connexion possible sans internet avec les comptes par défaut | Connexion impossible sans le service de données |

L'identifiant reste le même à l'écran (ex. `agent1`). En interne, il correspond à l'adresse
technique `agent1@pscc-idme.firebaseapp.com`. Aucun e-mail n'est envoyé à cette adresse.

## Étape 1 — Activer la connexion par mot de passe (1 minute)

1. Ouvrez la [console Firebase](https://console.firebase.google.com), projet **pscc-idme**.
2. Menu de gauche **Authentication** > **Commencer** (si ce bouton s'affiche).
3. Onglet **Sign-in method** > **E-mail/Mot de passe** > activez le premier interrupteur > **Enregistrer**.

## Étape 2 — Publier les règles de sécurité (1 minute)

1. Menu de gauche **Firestore Database** > onglet **Règles**.
2. Effacez tout le contenu et collez celui du fichier [`firestore.rules`](firestore.rules).
3. **Publier**.

> Dès cet instant, l'ancienne version de l'application ne peut plus lire les données :
> enchaînez directement avec l'étape 3.

## Étape 3 — Mettre la nouvelle version en ligne et créer votre compte

1. Remplacez l'ancien fichier sur votre hébergement par le nouveau `id-me-platform.html`.
2. Ouvrez le site (Ctrl + F5 pour éviter l'ancienne version en cache).
3. L'écran **« Première installation »** s'affiche : saisissez votre nom, un identifiant
   (ex. `direction`) et un mot de passe d'au moins 8 caractères.
4. Cliquez sur **Créer mon compte Super Admin** : vous êtes connecté.

L'écran de première installation disparaît définitivement dès que ce compte est créé.
Faites cette étape **sans attendre** après la mise en ligne : tant que le premier compte
n'existe pas, toute personne qui ouvre le site verrait cet écran. Si le message
« La première installation a déjà été faite » apparaît alors que vous n'avez rien créé,
contactez votre prestataire : quelqu'un l'a fait avant vous.

## Étape 4 — Recréer les comptes de l'équipe

1. Allez dans **Paramétrage > Utilisateurs**. Un encadré liste les **comptes de l'ancien
   système à recréer**.
2. Pour chaque compte : **Recréer…**, saisissez un **mot de passe provisoire**
   (8 caractères minimum), **Enregistrer**. Communiquez-le à la personne.
3. À sa première connexion, chaque utilisateur choisit son propre mot de passe.

Votre première connexion efface aussi les anciens mots de passe encore enregistrés dans la base.

## Si la connexion ne marche pas

| Message | Solution |
|---|---|
| « La connexion par mot de passe n'est pas encore activée » | Étape 1. |
| « Accès refusé par le service de données » | Étape 2 : les règles ne sont pas publiées. |
| « Identifiant ou mot de passe incorrect » | Tapez seulement l'identifiant (ex. `direction`), sans `@…`. |
| L'ancienne page s'affiche encore | Ctrl + F5 ou fenêtre privée. |

## Au quotidien

- **Ajouter un compte :** Paramétrage > Utilisateurs > Ajouter un utilisateur.
  Un Admin crée des Agents et des Responsables ; seul un Super Admin crée des Admins.
- **Retirer l'accès à quelqu'un :** bouton **Désactiver**. Il pourra être réactivé.
- **Changer son mot de passe :** bouton **Mot de passe** dans la barre latérale.
- **Mot de passe oublié :** Paramétrage > Utilisateurs > **Réinitialiser le mot de passe**
  à côté du compte. L'application affiche un **mot de passe provisoire** à transmettre à la
  personne ; elle devra en choisir un nouveau à sa connexion. Son identifiant, son rôle et son
  historique ne changent pas. (En coulisses, un nouvel accès est créé pour le même identifiant
  et l'ancien est désactivé : le plan gratuit de Firebase ne permet pas de modifier directement
  le mot de passe d'un autre compte.) Un Admin réinitialise les Agents et les Responsables ;
  seul un Super Admin réinitialise un Admin ou un autre Super Admin.
- **Sauvegarde :** l'export ne contient plus les comptes. Une restauration ne recrée pas
  les comptes, qui restent gérés par Firebase Authentication.

## Protections de la plateforme

- **Sessions :** la connexion ne dure que le temps de l'onglet. Fermer l'onglet ou le
  navigateur déconnecte (important sur un ordinateur partagé).
- **Inactivité :** déconnexion automatique après **30 minutes** sans activité.
- **Déconnexion :** la page est entièrement rechargée ; aucun dossier ne reste en mémoire,
  à l'écran ou dans la zone d'impression. Le bouton « Retour » ne réaffiche rien.
- **Compte désactivé ou rôle modifié** pendant qu'un utilisateur est connecté : il est
  déconnecté immédiatement, avec un message.
- **Textes saisis :** tous les textes (noms, communes, listes, journal…) sont neutralisés avant
  affichage ; un code écrit dans un champ ne peut pas s'exécuter chez un autre utilisateur.
- **Politique de sécurité du contenu (CSP) :** le navigateur n'exécute que les scripts de la
  plateforme et de Firebase. **Après toute modification d'un script de `id-me-platform.html`,
  lancer `python3 tools/update-csp.py`**, sinon la plateforme ne démarre plus.

### En-têtes conseillés sur LWS (fichier `.htaccess`)

À **ajouter** à la fin du fichier `.htaccess` existant (sans effacer ce qu'il contient) :

```
<IfModule mod_headers.c>
  Header always set X-Frame-Options "DENY"
  Header always set Content-Security-Policy "frame-ancestors 'none'"
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "same-origin"
  <FilesMatch "\.html$">
    Header set Cache-Control "no-store"
  </FilesMatch>
</IfModule>
```

Ils empêchent d'afficher la plateforme dans le cadre d'un autre site (piège au clic) et
évitent que le navigateur garde une copie des pages.

## Pour aller plus loin

- **Plan Blaze (payant) :** permettrait de supprimer réellement un compte depuis l'application,
  via une petite fonction côté serveur.
- **Clé API Firebase :** elle est visible dans le code, c'est normal pour une application web.
  La protection vient des règles de sécurité de l'étape 4. Vous pouvez en plus restreindre la clé
  à votre nom de domaine dans Google Cloud Console > API et services > Identifiants.
