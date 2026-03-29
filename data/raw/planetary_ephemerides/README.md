# Planetary Ephemerides – Rohdaten

## Quelle
JPL (Jet Propulsion Laboratory)  
Ephemeriden-Serien: DE430, DE440 oder vergleichbare NASA‑Ephemeriden

## Inhalt
Dieser Ordner enthält die unverarbeiteten Ephemeriden der Planeten und relevanten Monde.

Typische enthaltene Datensätze:

- Heliocentrische Positionen (x, y, z)
- Geschwindigkeiten (vx, vy, vz)
- Bahnparameter (a, e, i, Ω, ω, M)
- Zeitstempel im Julian Date Format
- Optional: baryzentrische Koordinaten

## Format
Die Daten liegen üblicherweise in folgenden Formaten vor:

- `.txt`
- `.csv`
- `.json`
- `.eph` (JPL‑Format)

## Verwendung im Projekt
Die Ephemeriden dienen als Grundlage für:

- Berechnung planetarer Zyklen  
- Identifikation von Resonanzen  
- Kopplung planetarer Perioden mit solaren und galaktischen Modulationen  
- Modelle in `analysis/zyklusanalyse.ipynb`  
- Interferenzmodelle in `analysis/zeitfeld_interferenz.ipynb`

## Verarbeitung
Die Rohdaten werden später in:

`data/processed/zyklusfrequenzen/`

überführt.
