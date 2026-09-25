# Sécurité de la connexion — mise en place

L'application vérifie désormais les mots de passe avec **Firebase Authentication**.
Les mots de passe ne sont plus écrits dans le code ni enregistrés dans Firestore, et les
données ne sont accessibles qu'aux comptes connectés et actifs.

> **Important :** tant que les étapes 1 à 4 ne sont pas faites, **personne ne peut se connecter**
> avec la nouvelle version. Faites-les avant de mettre la nouvelle version en ligne.

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

## Étape 1 — Activer la connexion par mot de passe

1. Ouvrez la [console Firebase](https://console.firebase.google.com), projet **pscc-idme**.
2. Menu **Authentication** > **Commencer** (si ce n'est pas déjà fait).
3. Onglet **Sign-in method** > **E-mail/Mot de passe** > **Activer** > **Enregistrer**.

## Étape 2 — Créer le premier compte Super Admin

1. **Authentication** > onglet **Users** > **Ajouter un utilisateur**.
2. Adresse e-mail : `VOTRE-IDENTIFIANT@pscc-idme.firebaseapp.com`
   (par exemple `direction@pscc-idme.firebaseapp.com` ; l'identifiant en minuscules,
   3 à 32 caractères : lettres, chiffres, point, tiret).
3. Mot de passe : au moins 8 caractères, que vous seul connaissez.
4. Une fois créé, **copiez l'UID** affiché dans la liste (une suite de lettres et de chiffres).

## Étape 3 — Créer son profil dans Firestore

1. **Firestore Database** > onglet **Données** > **Commencer une collection**.
2. ID de la collection : `users`.
3. ID du document : **collez l'UID** copié à l'étape 2.
4. Ajoutez ces champs :

| Champ | Type | Valeur |
|---|---|---|
| `username` | string | votre identifiant (ex. `direction`) |
| `nom` | string | votre nom complet |
| `role` | string | `Super Admin` |
| `active` | boolean | `true` |

5. **Enregistrer**.

## Étape 4 — Publier les règles de sécurité

1. **Firestore Database** > onglet **Règles**.
2. Remplacez tout le contenu par celui du fichier [`firestore.rules`](firestore.rules).
3. **Publier**.

À partir de ce moment, la base n'est plus ouverte : seuls les comptes créés comme ci-dessus
peuvent lire ou modifier les dossiers.

## Étape 5 — Première connexion et recréation des comptes

1. Ouvrez l'application et connectez-vous avec l'identifiant et le mot de passe de l'étape 2.
   **Connectez-vous en Super Admin avant tout autre utilisateur** : c'est cette connexion qui
   efface les anciens mots de passe de `appdata/config`.
2. Allez dans **Paramétrage > Utilisateurs**. Un encadré liste les **comptes de l'ancien
   système à recréer**.
3. Pour chaque compte : cliquez sur **Recréer…**, saisissez un **mot de passe provisoire**
   (8 caractères minimum), **Enregistrer**. Communiquez ce mot de passe à la personne.
4. À sa première connexion, chaque utilisateur doit choisir son propre mot de passe.

## Au quotidien

- **Ajouter un compte :** Paramétrage > Utilisateurs > Ajouter un utilisateur.
  Un Admin crée des Agents et des Responsables ; seul un Super Admin crée des Admins.
- **Retirer l'accès à quelqu'un :** bouton **Désactiver**. Il pourra être réactivé.
- **Changer son mot de passe :** bouton **Mot de passe** dans la barre latérale.
- **Mot de passe oublié :** avec le plan gratuit de Firebase, un administrateur ne peut pas
  changer le mot de passe d'un autre depuis l'application (et l'envoi d'un e-mail de
  réinitialisation ne marche pas, l'adresse étant technique). Procédure :
  1. dans l'application, **Désactivez** le compte ;
  2. dans la console, **Authentication > Users**, supprimez le compte (menu ⋮ > Supprimer) ;
  3. dans l'application, recréez-le avec le **même identifiant** et un mot de passe provisoire.

  L'ancien profil reste affiché comme « Désactivé » ; il ne permet plus aucune connexion.
- **Sauvegarde :** l'export ne contient plus les comptes. Une restauration ne recrée pas
  les comptes, qui restent gérés par Firebase Authentication.

## Pour aller plus loin

- **Plan Blaze (payant) :** permettrait à un administrateur de réinitialiser le mot de passe
  d'un autre utilisateur ou de supprimer un compte directement depuis l'application,
  via une petite fonction côté serveur.
- **Clé API Firebase :** elle est visible dans le code, c'est normal pour une application web.
  La protection vient des règles de sécurité de l'étape 4. Vous pouvez en plus restreindre la clé
  à votre nom de domaine dans Google Cloud Console > API et services > Identifiants.
