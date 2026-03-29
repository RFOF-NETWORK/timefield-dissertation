"""
plotting.py
-----------

Zweck:
    Zentrale Sammlung aller Visualisierungs- und Plot-Funktionen für das
    gesamte Zeitfeld-Projekt. Dieses Modul stellt standardisierte,
    reproduzierbare und wissenschaftlich saubere Diagramme bereit.

Hauptfunktionen:
    - plot_fft(frequencies, amplitudes, title=None)
    - plot_wavelet(time, scales, coefficients)
    - plot_tensorfield(tensor, projection="2d")
    - plot_interference_spectrum(freqs, power)
    - save_figure(path, dpi=300)

Eingaben:
    - numerische Arrays (NumPy)
    - Tensorfelder
    - Frequenzspektren
    - Zeitreihen
    - optionale Layout-Parameter

Ausgaben:
    - Diagramme (Matplotlib-Figuren)
    - exportierte Grafiken (.png, .svg, .pdf)
    - Visualisierungen für presentation/figures/

Abhängigkeiten:
    - matplotlib.pyplot
    - numpy
    - seaborn (optional)
    - constants (für Achsenbeschriftungen, physikalische Parameter)

Verwendung:
    Wird genutzt von:
        - allen Notebooks in analysis/
        - allen Skripten in tools/scripts/
        - Präsentations- und Poster-Generierung
"""
