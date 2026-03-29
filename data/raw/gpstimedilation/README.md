# GPS Time Dilation – Rohdaten

## Quelle
GNSS / GPS Systemdaten  
(US Naval Observatory, NIST, IGS – International GNSS Service)

## Inhalt
Dieser Ordner enthält die unverarbeiteten Messdaten zur relativistischen Zeitdilatation in GPS‑Satelliten.

Typische enthaltene Datensätze:

- Satellitenbahnhöhen  
- Orbitalparameter  
- Atomuhren‑Drift  
- Relativistische Korrekturen (SRT + ART)  
- Signalverzögerungen  
- Zeitstempel (GPS Time, UTC, TAI)

## Format
Die Daten liegen üblicherweise in folgenden Formaten vor:

- `.csv`
- `.rinex`
- `.txt`
- `.json`

## Verwendung im Projekt
Die GPS‑Zeitdilatationsdaten dienen als Grundlage für:

- Validierung der relativistischen Komponenten des Zeitfeldmodells  
- Vergleich zwischen theoretischen und gemessenen Zeitdifferenzen  
- Modelle in `analysis/relativistische_korrekturen.ipynb`  
- Kopplung mit solaren und planetaren Modulationen

## Verarbeitung
Die Rohdaten werden später in:

`data/processed/zeitgradienten/`

überführt.
