# Design System — IDME Cameroun (MASTER)

> **Règle :** avant de construire une page, vérifier si `design-system/idme-cameroun/pages/<nom-de-page>.md` existe.
> Si oui, ses règles **remplacent** celles de ce fichier. Sinon, appliquer strictement ce fichier.

---

**Projet :** IDME Cameroun — gestion des documents d'identité (CNI, passeport, actes de naissance)
**Catégorie (skill UI UX Pro Max) :** Government/Public Service
**Style de base :** République Accessible — *Accessible & Ethical + Inclusive Design*
**Périmètre :** espace citoyen (par défaut, toutes pages). Surcharges :
- `pages/espace-agent.md` — back-office des agents (Data-Dense Dashboard + mode sombre optionnel)
- `pages/document-officiel.md` — documents délivrés et vérification d'authenticité (Autorité & Sceau)

**Origine :** généré avec le skill UI UX Pro Max (`--design-system`), puis palette adaptée à l'identité
camerounaise (le skill propose par défaut du bleu marine). Chaque couleur de texte a été vérifiée
au ratio de contraste WCAG indiqué.

---

## Palette de couleurs

| Rôle | Hex | Variable CSS | Contraste | Origine |
|------|-----|--------------|-----------|---------|
| Primaire (vert national) | `#006B3F` | `--color-primary` | 6,6:1 sur blanc | adapté |
| Sur primaire | `#FFFFFF` | `--color-on-primary` | — | skill |
| Secondaire | `#334155` | `--color-secondary` | — | skill |
| Sur secondaire | `#FFFFFF` | `--color-on-secondary` | — | skill |
| Accent / liens | `#0369A1` | `--color-accent` | 5,9:1 sur blanc | skill |
| Sur accent | `#FFFFFF` | `--color-on-accent` | — | skill |
| Mise en avant (drapeau) | `#FCD116` | `--color-highlight` | fond uniquement, texte `#0F172A` dessus (12,1:1) | adapté |
| Fond | `#F8FAFC` | `--color-background` | — | skill |
| Texte principal | `#0F172A` | `--color-foreground` | 17,1:1 | skill |
| Carte | `#FFFFFF` | `--color-card` | — | skill |
| Texte sur carte | `#0F172A` | `--color-card-foreground` | 17,9:1 | skill |
| Zone atténuée | `#E8ECF1` | `--color-muted` | — | skill |
| Texte secondaire | `#475569` | `--color-muted-foreground` | 7,2:1 | skill |
| Bordures | `#E2E8F0` | `--color-border` | — | skill |
| Erreur / alerte | `#CE1126` | `--color-destructive` | 5,6:1 sur blanc | adapté (rouge drapeau) |
| Sur erreur | `#FFFFFF` | `--color-on-destructive` | — | skill |
| Succès | `#15803D` | `--color-success` | 5,0:1 sur blanc | adapté |
| Contour de focus | `#0F172A` | `--color-ring` | — | skill |

**Usage des couleurs du drapeau :** en petites touches (bandeau fin en haut de page, badges, séparateurs).
Jamais de grands aplats tricolores. Le jaune `#FCD116` n'est **jamais** utilisé comme couleur de texte.

## Typographie

- **Titres et texte :** Atkinson Hyperlegible (paire « Accessibility First » du skill)
- **Numéros de dossier / CNI :** IBM Plex Mono (voir `pages/document-officiel.md`)
- **Taille minimale du texte courant :** 16px, interligne 1,5
- **Humeur :** accessible, lisible, inclusif, adapté à la dyslexie

```css
@import url('https://fonts.googleapis.com/css2?family=Atkinson+Hyperlegible:wght@400;700&display=swap');
```

## Espacements

| Variable | Valeur | Usage |
|----------|--------|-------|
| `--space-xs` | `4px` | Écarts serrés |
| `--space-sm` | `8px` | Icône + texte |
| `--space-md` | `16px` | Marge intérieure standard |
| `--space-lg` | `24px` | Marge de section |
| `--space-xl` | `32px` | Grands écarts |
| `--space-2xl` | `48px` | Marges entre sections |
| `--space-3xl` | `64px` | En-tête de page |

## Ombres

| Niveau | Valeur | Usage |
|--------|--------|-------|
| `--shadow-sm` | `0 1px 2px rgba(0,0,0,0.05)` | Léger relief |
| `--shadow-md` | `0 4px 6px rgba(0,0,0,0.1)` | Cartes, boutons |
| `--shadow-lg` | `0 10px 15px rgba(0,0,0,0.1)` | Fenêtres, menus |

---

## Composants

### Boutons

```css
.btn-primary {
  background: var(--color-primary);      /* #006B3F */
  color: var(--color-on-primary);
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 700;
  transition: background-color 200ms ease;
  cursor: pointer;
}
.btn-primary:hover { background: #005532; }

.btn-secondary {
  background: transparent;
  color: var(--color-foreground);
  border: 2px solid var(--color-foreground);
  min-height: 44px;
  padding: 12px 24px;
  border-radius: 8px;
  font-weight: 700;
  cursor: pointer;
}

:focus-visible { outline: 3px solid var(--color-ring); outline-offset: 2px; }
```

### Cartes

```css
.card {
  background: var(--color-card);
  border: 1px solid var(--color-border);
  border-radius: 12px;
  padding: 24px;
  box-shadow: var(--shadow-sm);
}
/* cursor:pointer et effet de survol uniquement si la carte entière est cliquable */
```

### Champs de formulaire

```css
.input {
  min-height: 44px;
  padding: 12px 16px;
  border: 1px solid #94A3B8;           /* bordure de champ ≥ 3:1 */
  border-radius: 8px;
  font-size: 16px;
}
.input:focus-visible { outline: 3px solid var(--color-ring); outline-offset: 1px; }
.input[aria-invalid="true"] { border-color: var(--color-destructive); }
```

Règles formulaire : libellé visible au-dessus de chaque champ (jamais le placeholder seul),
texte d'aide sous le champ, message d'erreur juste sous le champ concerné **et** récapitulatif
des erreurs en haut du formulaire, champs longs découpés en étapes numérotées.

### Statuts de dossier

Toujours **icône + libellé + couleur** (jamais la couleur seule) :

| Statut | Couleur | Icône (Lucide) |
|--------|---------|----------------|
| Déposé | `#475569` | `file-text` |
| En instruction | `#0369A1` | `clock` |
| Pièce manquante | `#92400E` | `alert-triangle` |
| Validé / prêt au retrait | `#15803D` | `check-circle` |
| Rejeté | `#CE1126` | `x-circle` |

---

## Style et structure des pages

**Style :** Accessible & Ethical — contrastes élevés, texte ≥ 16px, focus visible 3–4px,
liens d'évitement (« Aller au contenu »), zones tactiles ≥ 44×44px, `prefers-reduced-motion` respecté.

**Modèle de page (skill) :** Minimal Single Column — une action principale par écran,
grande typographie, beaucoup d'espace, pensé mobile d'abord.

**Portail d'accueil :** Service Directory + Search — recherche en haut, puis les démarches
(CNI, passeport, acte de naissance, suivi de dossier) en cartes.

**Contexte camerounais :** interface en français (prévoir l'anglais, pays bilingue),
pages légères pour les connexions 3G, montants en FCFA, formats de date JJ/MM/AAAA.

---

## Anti-patterns (à ne pas utiliser)

- ❌ Décor chargé, grands motifs, dégradés
- ❌ Contraste faible (gris sur gris)
- ❌ Animations décoratives
- ❌ Emojis comme icônes — utiliser des icônes SVG (Lucide)
- ❌ Statut indiqué par la couleur seule
- ❌ Placeholder utilisé comme seul libellé
- ❌ Contour de focus supprimé
- ❌ Survols qui décalent la mise en page

---

## Checklist avant livraison

- [ ] Aucune icône emoji (SVG uniquement, un seul jeu d'icônes)
- [ ] `cursor: pointer` sur tous les éléments cliquables
- [ ] Transitions de 150–300ms sur les changements d'état
- [ ] Contraste texte ≥ 4,5:1 (vérifié)
- [ ] Focus visible au clavier sur tous les éléments interactifs
- [ ] `prefers-reduced-motion` respecté
- [ ] Responsive testé à 375px, 768px, 1024px, 1440px
- [ ] Aucun contenu masqué par une barre fixe
- [ ] Pas de défilement horizontal sur mobile
