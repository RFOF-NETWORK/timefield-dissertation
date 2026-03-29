# GAIA – Rohdaten

## Quelle
ESA GAIA Mission (DR2/DR3)

## Inhalt
Dieser Ordner enthält die unverarbeiteten GAIA-Daten, die für die Modellierung der galaktischen Zeitgradienten verwendet werden.

Typische enthaltene Datensätze:

- Sternpositionen (RA, DEC)
- Parallaxen
- Eigenbewegungen
- Radialgeschwindigkeiten
- Photometrische Messungen

## Format
Die Daten liegen üblicherweise in folgenden Formaten vor:

- `.csv`
- `.fits`
- `.parquet`

## Verwendung im Projekt
Die GAIA-Daten dienen als Grundlage für:

- Rekonstruktion galaktischer Potentiale  
- Berechnung großskaliger Zeitgradienten  
- Ableitung von Dichte- und Geschwindigkeitsverteilungen  
- Vorbereitung der Modelle in `analysis/galaktische_zeitgradienten.ipynb`

## Verarbeitung
Die Rohdaten werden später in:

`data/processed/gravitationsprofile/`

überführt.
