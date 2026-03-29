# Tools – Utilities

## Zweck
Dieser Ordner enthält alle Hilfs‑ und Dienstprogramme, die von Skripten, Notebooks und Datenpipelines im gesamten Projekt genutzt werden.  
Die Utilities stellen grundlegende Funktionen bereit, die in mehreren Modulen wiederverwendet werden und die technische Basis des Zeitfeld‑Frameworks stabilisieren.

## Enthaltene Module

### `plotting.py`
Zentrale Sammlung aller Plot‑ und Visualisierungsfunktionen.

Funktionen:
- Standardisierte Diagramm‑Layouts  
- Fourier‑ und Wavelet‑Plots  
- Tensorfeld‑Visualisierungen  
- Interferenzdiagramme  
- Exportfunktionen für `presentation/figures/`  

Wird verwendet von:
- `analysis/*`  
- `tools/scripts/fourier_zyklen.py`  
- `presentation/*`  

---

### `constants.py`
Definiert alle physikalischen, astronomischen und projektspezifischen Konstanten.

Beispiele:
- Gravitationskonstanten  
- Solare Parameter  
- Planetare Bahndaten  
- Zeitkonstanten (UTC, TAI, GPS Time)  
- Modellparameter für das Zeitfeld  

Wird verwendet von:
- allen Skripten in `tools/scripts/`  
- allen Notebooks in `analysis/`  

---

### `astro_helpers.py`
Hilfsfunktionen für astronomische Berechnungen.

Funktionen:
- Umrechnung astronomischer Koordinaten  
- Julian Date / GPS Time / UTC Konvertierungen  
- Ephemeriden‑Interpolation  
- Berechnung orbitaler Parameter  
- Transformationen für galaktische Koordinaten  

Wird verwendet von:
- `tools/scripts/zeitfeld_tensor_generator.py`  
- `tools/scripts/fourier_zyklen.py`  
- `analysis/galaktische_zeitgradienten.ipynb`  
- `analysis/zyklusanalyse.ipynb`  

---

## Verwendung
Die Utilities bilden die technische Basis für:

- Datenverarbeitung  
- Modellberechnung  
- Visualisierung  
- Zeitfeld‑Tensoren  
- Frequenzanalysen  
- Interferenzmodelle  

Sie werden projektweit importiert und dienen als stabile, wiederverwendbare Funktionsbibliothek.

## Status
Dieser Ordner ist vollständig und stellt die Kern‑Utilities des Zeitfeld‑Frameworks bereit.
