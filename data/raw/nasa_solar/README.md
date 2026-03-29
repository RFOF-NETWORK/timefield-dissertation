# NASA Solar – Rohdaten

## Quelle
NASA / NOAA Solar Observatories  
(SDO, SOHO, GOES, SILSO, OMNI)

## Inhalt
Dieser Ordner enthält die unverarbeiteten solaren Aktivitätsdaten, die für die Analyse der solaren Zeitmodulationen verwendet werden.

Typische enthaltene Datensätze:

- Sonnenfleckenzahlen (Daily, Monthly)
- Flares (X‑Ray, Proton Events)
- Magnetfeldmessungen (Magnetogramme)
- Solare Zyklen (Schwabe, Hale, Gleissberg)
- TSI (Total Solar Irradiance)
- Solar Wind Parameter

## Format
Die Daten liegen üblicherweise in folgenden Formaten vor:

- `.csv`
- `.json`
- `.txt`
- `.fits`

## Verwendung im Projekt
Die NASA‑Solar‑Daten dienen als Grundlage für:

- Analyse solarer Zyklen  
- Identifikation von Frequenzen und Resonanzen  
- Interferenz mit planetaren und galaktischen Zeitfeldern  
- Modelle in `analysis/zyklusanalyse.ipynb`  
- Kopplungsmodelle in `analysis/zeitfeld_interferenz.ipynb`

## Verarbeitung
Die Rohdaten werden später in:

`data/processed/zyklusfrequenzen/`

überführt.
