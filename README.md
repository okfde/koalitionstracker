# Koalitionstracker 2021

## Projektplan

1. Koalitionsvertrag in Vorhaben aufspalten
2. Ggf. priorisieren und kontextualisieren
3. Redaktionelle Begleitung des Fortschritts


## Mitmachen

Wir sind in Phase 1: Koalitionsvertrag in Vorhaben aufspalten. Pull Requests um Vorhaben in den Kapiteln zu identifizieren werden gerne entgegengenommen.

Ein Vorhaben definieren wir als steuerbare und überprüfbare politische Veränderung, wie die Einführung eines Gesetzes oder die Änderung einer Verordnung.

Um ein Vorhaben zu markieren, kann als einfachster Schritt ein Markdown-Link um das jeweilige Vorhaben gesetzt werden: 

```
[Vorhabens-Text](#vorhaben-id)
```

## Technik

Der Koalitionsvertrag findet sich mit seinen Kapiteln in `_chapters`.

Im YAML-Frontmatter werden die Vorhaben gesammelt und folgendermaßen gegliedert:

```
statements:
  - summary: "Straftatbestand der Abgeordnetenbestechung und -bestechlichkeit wirksamer ausgestalten"
    status: "not_implemented"
    id: html-id
    categories:
      - Category 1
      - Category 2
    last_update:
    reports:
      - title: "Test"
        url: "http://example.org"
```

- `summary` ist die Kurzform des Vorhabens

- `status` kann folgende Werte haben:

  - `not_implemented` - damit geht's los
  - `partially_implemented` - Teile des Vorhabens wurden umgesetzt
  - `implemented` - Das Vorhaben wurde umgesetzt
  - `broken` - Das Vorhaben wurde verpasst (zeitlich) oder das Gegenteil getan

- `categories` Themengebiete, Schlagworte

- `id` soll die Textreferenz sein

- `last_update` sollte ein Datum sein

- `reports` ist eine Liste von Links zu Nachrichtenartikeln, die den Status beschreiben oder belegen.
