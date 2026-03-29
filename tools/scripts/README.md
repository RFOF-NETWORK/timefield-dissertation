# Tools – Scripts

## Zweck
Dieser Ordner enthält alle Skripte, die zur Verarbeitung, Analyse und Modellierung der Zeitfeld‑Daten benötigt werden.  
Die Skripte bilden die technische Grundlage für:

- Datenbereinigung  
- Frequenzanalysen  
- Tensorfeld‑Generierung  
- Automatisierte Verarbeitungspipelines  

## Enthaltene Skripte

### `fourier_zyklen.py`
Führt Fourier‑Analysen auf solaren, planetaren und galaktischen Zeitreihen durch.  
Typische Funktionen:

- Berechnung von Amplitudenspektren  
- Identifikation dominanter Frequenzen  
- Erkennung von Resonanzclustern  
- Export von Spektren für `data/processed/zyklusfrequenzen/`

### `zeitfeld_tensor_generator.py`
Erzeugt Tensorfelder für die fünf Schichten des Zeitfeldmodells.  
Funktionen:

- Aufbau von Gradient‑Tensoren  
- Interferenz‑Tensoren  
- Kopplung galaktischer, solarer und planetarer Felder  
- Export nach `data/processed/gravitationsprofile/` und `data/processed/zeitgradienten/`

### `datenbereinigung.py`
Bereinigt und harmonisiert Rohdaten aus:

- GAIA  
- NASA Solar  
- Planetary Ephemerides  
- GPS Time Dilation  

Funktionen:

- Entfernen fehlerhafter Messpunkte  
- Interpolation fehlender Werte  
- Normalisierung  
- Zeitachsen‑Synchronisation  

## Verwendung
Die Skripte werden genutzt von:

- Notebooks in `analysis/`  
- Tools in `tools/utilities/`  
- Datenpipelines für `data/processed/`

## Status
Alle Skripte in diesem Ordner sind operative Werkzeuge für die Datenverarbeitung und Modellgenerierung.
