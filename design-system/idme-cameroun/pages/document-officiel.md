# Surcharge — Document officiel et vérification

> Remplace `MASTER.md` pour : aperçu d'un document délivré (CNI, passeport, acte de naissance),
> récépissé de dépôt, page publique de vérification d'authenticité (QR code / numéro).

**Style :** Autorité & Sceau — palette « Legal Services » du skill (*Authority navy + trust gold*),
où le vert national remplace le marine.

## Palette

| Rôle | Hex | Contraste | Origine |
|------|-----|-----------|---------|
| Primaire | `#064E3B` | 8,6:1 sur papier | adapté |
| Fond « papier sécurisé » | `#F4F1E8` | — | adapté |
| Filigrane / guillochis | `#DCE6E0` | décoratif | adapté |
| Or (texte, libellés) | `#92400E` | 6,3:1 sur papier | adapté (le skill propose `#B45309`, trop clair sur ce fond) |
| Or du sceau | `#B08D3C` | 3,1:1 — **décoratif uniquement, jamais pour du texte** | adapté |
| Rouge tampon | `#9E2A2B` | 6,6:1 sur papier | adapté |
| Texte | `#0F172A` | — | skill |
| Bordures / liserés | `#CBD5E1` | — | skill |

## Typographie

- **Texte :** IBM Plex Sans (paire « Financial Trust » du skill)
- **Numéros de CNI, de dossier, de passeport, zone MRZ :** IBM Plex Mono, espacement des lettres élargi
  pour la lecture et la saisie

```css
@import url('https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;500;700&display=swap');
```

## Éléments visuels

- Liseré fin vert/rouge/jaune en haut du document
- Filigrane guilloché en fond (SVG, opacité faible, `aria-hidden="true"`)
- Sceau circulaire doré avec l'état du document
- Tampon de statut : « AUTHENTIQUE » (vert `#064E3B`) ou « NON VALIDE » (rouge `#9E2A2B`),
  toujours accompagné d'une icône et d'un texte explicatif

## Règles spécifiques

- La page de vérification affiche un résultat clair en une phrase, avant tout détail
- Données personnelles minimales sur la page publique de vérification (nom partiel, date de délivrance, statut)
- Version imprimable (`@media print`) sans fond ni filigrane
- Ne jamais imiter l'apparence exacte d'un document officiel réel (pas de reproduction des armoiries
  ni de maquette fidèle de la CNI) : l'aperçu reste une représentation d'interface
