# Surcharge — Espace agent (back-office)

> Remplace `MASTER.md` pour les écrans des agents : liste des dossiers, instruction, validation,
> statistiques. Tout ce qui n'est pas précisé ici reste régi par `MASTER.md`.

**Style :** Data-Dense Dashboard (skill UI UX Pro Max), avec mode sombre optionnel (Dark Mode OLED).
**Densité :** élevée — espacements 8–32px.

## Palette — mode clair (par défaut)

| Rôle | Hex | Contraste | Origine |
|------|-----|-----------|---------|
| Fond de page | `#F5F5F5` | — | skill |
| Cartes / tableaux | `#FFFFFF` | — | skill |
| Texte | `#333333` | 11,6:1 sur `#F5F5F5` | skill |
| Primaire | `#006B3F` | 6,1:1 sur `#F5F5F5` | adapté (MASTER) |
| Statut « en instruction » | `#0369A1` | 5,9:1 sur blanc | skill |
| Statut « validé » | `#15803D` | 5,0:1 sur blanc | adapté |
| Statut « rejeté » | `#B91C1C` | ≥ 6:1 sur blanc | adapté |

Les statuts sont affichés dans les cartes et tableaux blancs, pas directement sur le fond gris.

## Palette — mode sombre (option)

| Rôle | Hex | Contraste | Origine |
|------|-----|-----------|---------|
| Fond | `#0E1512` | — | adapté (le skill propose `#121212`) |
| Surfaces | `#18221D` | — | adapté |
| Bordures | `#2C3A33` | — | adapté |
| Texte | `#E8EDE9` | 15,6:1 | adapté |
| Texte secondaire | `#9AA7A0` | 6,5:1 sur surface | adapté |
| Primaire | `#3FB27F` | 6,1:1 sur surface | adapté |
| Accent | `#E8C35A` | 9,6:1 sur surface | adapté |
| Info | `#6CB7F0` | 7,5:1 sur surface | adapté |
| Erreur | `#F0736A` | 5,7:1 sur surface | adapté |

Bouton primaire en mode sombre : fond `#3FB27F`, texte `#0E1512` (6,9:1).
Le choix clair/sombre suit `prefers-color-scheme` et peut être forcé par l'agent.

## Typographie

- **Interface :** Fira Sans (paire « Dashboard Data » du skill)
- **Identifiants, numéros de dossier, journaux :** Fira Code
- Chiffres tabulaires (`font-variant-numeric: tabular-nums`) dans les tableaux

```css
@import url('https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500&family=Fira+Sans:wght@400;500;700&display=swap');
```

## Espacements

| Variable | Valeur |
|----------|--------|
| `--space-xs` | `4px` |
| `--space-sm` | `8px` |
| `--space-md` | `12px` |
| `--space-lg` | `16px` |
| `--space-xl` | `24px` |
| `--space-2xl` | `32px` |

## Règles spécifiques

- Tableaux : en-tête collant, tri et filtres visibles, pagination ou virtualisation au-delà de 100 lignes
- Actions de validation/rejet : confirmation obligatoire pour le rejet, motif de rejet requis
- Indicateurs en haut : dossiers en attente, en retard, traités aujourd'hui
- Raccourcis clavier pour les actions fréquentes, tous documentés
- Zones tactiles ≥ 44×44px conservées même en densité élevée
