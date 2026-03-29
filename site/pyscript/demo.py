# site/pyscript/demo.py
from math import sqrt

def relativistic_time_dilation(v, c=3e8):
    gamma = 1.0 / sqrt(1.0 - (v**2 / c**2))
    return 1.0 / gamma

def gravitational_time_dilation(M, r, G=6.674e-11, c=3e8):
    factor = (1.0 - (2 * G * M) / (r * c**2)) ** 0.5
    return factor

v = 10000.0  # m/s
M_earth = 5.972e24  # kg
r_earth = 6.371e6   # m

rel = relativistic_time_dilation(v)
grav = gravitational_time_dilation(M_earth, r_earth)

print(f"Relativistische Zeitdilatation (v={v} m/s): {rel:.12f}")
print(f"Gravitative Zeitdilatation (Erde-Oberfläche): {grav:.12f}")
print("Symbolische kombinierte Zeitfeld-Komponente T = T_rel + T_grav ≈", f"{rel + grav:.12f}")
