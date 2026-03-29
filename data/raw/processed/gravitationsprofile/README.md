# Gravitationsprofile – Verarbeitete Daten

## Inhalt
Dieser Ordner enthält die aus den Rohdaten abgeleiteten Gravitationsprofile und Potentialmodelle.  
Die Profile beschreiben die räumliche Struktur von Gravitationsfeldern auf:

- galaktischer Ebene  
- solarer Ebene  
- planetarer Ebene  

sowie deren Einfluss auf Zeitmodulationen.

## Herkunft der Daten
Die Daten in diesem Ordner entstehen aus der Verarbeitung folgender Rohdaten:

- `data/raw/gaia/`  
- `data/raw/planetary_ephemerides/`  
- `data/raw/nasa_solar/`  

## Typische Dateien
- `galaktisches_potential.npy`  
- `solares_gravitationsmodell.json`  
- `planetare_potentialprofile.csv`  
- `gradient_tensorfelder.parquet`  
- `massendichte_modelle/` (Unterordner)

## Verwendung im Projekt
Diese Gravitationsprofile werden genutzt in:

- `analysis/galaktische_zeitgradienten.ipynb`  
- `analysis/relativistische_korrekturen.ipynb`  
- `analysis/zeitfeld_interferenz.ipynb`  

Sie bilden die Grundlage für:

- Tensorfeld‑Berechnungen  
- Gradientenmodelle  
- Interferenzsimulationen  
- Kopplung der fünf Zeitfeld‑Schichten

## Format
Die Dateien liegen in folgenden Formaten vor:

- `.npy`  
- `.json`  
- `.csv`  
- `.parquet`

## Status
Alle Daten in diesem Ordner sind **bereits verarbeitet** und können direkt in den Analyse‑Notebooks geladen werden.
