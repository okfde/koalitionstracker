# Koalitionstracker 2021

Der Koalitionsvertrag findet sich mit seinen Kapiteln in `_chapters`.

Im YAML-Frontmatter werden die Vorhaben gesammelt und folgendermaßen gegliedert:

```
statements:
  - summary: "Straftatbestand der Abgeordnetenbestechung und -bestechlichkeit wirksamer ausgestalten"
    status: "not_implemented"
    id:
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