# Aero-Structural Analysis of the NREL 5MW Wind Turbine #

[![Python](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Issues](https://img.shields.io/github/issues/YOURUSERNAME/NREL-5MW-Analysis)](https://github.com/YOURUSERNAME/NREL-5MW-Analysis/issues)
[![PRs](https://img.shields.io/github/issues-pr/YOURUSERNAME/NREL-5MW-Analysis)](https://github.com/YOURUSERNAME/NREL-5MW-Analysis/pulls)



This project explores the aero-structural characteristics of the NREL 5MW Reference Wind Turbine, using the publicly available blade definition data published in NREL Technical Report TP-500-38060.

My goal was to take the raw, discrete blade properties (only 17 defined stations) and build a smooth, high-resolution representation suitable for engineering analysis.



Rather than treating this as a simple plotting task, I approached it the way real computational engineers doing by reconstructing missing information, interpolating geometric profiles, and evaluating stiffness trends along the blade span.



\## Project Summary



Wind turbine blades are rarely defined point-by-point. Instead, they’re given at a handful of radial stations, and engineers must reconstruct the full geometry before running CFD or structural simulations.



In this project:



\* Imported the official Chord, Twist, and Airfoil distributions from NREL.

\* Used cubic spline interpolation to rebuild the full 61.5 m blade profile.

\* Estimated relative bending stiffness along the span using a simple area moment proxy.

\* Visualized key aerodynamic and structural variables to understand design intent and load patterns.



The final result is a clean, reproducible workflow that converts raw reference data into a simulation ready dataset.



\## Tools \& Libraries



\* Python — Core scripting

\* Pandas — Data structuring

\* SciPy (interp1d) — Cubic spline interpolation

\* NumPy — Numerical operations

\* Matplotlib / Seaborn — Plotting and profile visualization



\## Methodology



\### 1. Input Data



The script begins with the blade definition table from the NREL report. These values describe the blade at only 17 radial stations, from the root all the way to the tip.



\### 2. Geometry Reconstruction



Because CFD and FEA require smooth, high-resolution geometry, I interpolated:



\* Chord length

\* Twist angle

\* Thickness ratio

\* Airfoil transitions



Using cubic splines allowed the blade shape to remain smooth (second-order continuous), which is important for accurate aerodynamic performance.



\### 3. Structural Stiffness Estimation



To approximate how the blade handles bending loads, I calculated a relative stiffness parameter using a simple engineering proxy:



&nbsp;						I ∝ c^3 · t



Where:



\* c = chord

\* t = thickness ratio



This highlights the expected stiffness concentration in the root region (0–15 m), where bending moments are highest.



\## How to Run the Project



1\. Clone the repository



```bash

git clone https://github.com/YOURUSERNAME/NREL-5MW-Analysis.git

cd NREL-5MW-Analysis

```



2\. Install dependencies



```bash

pip install -r requirements.txt

```



3\. Run the analysis



```bash

python src/nrel\_blade\_analysis.py

```



4\. View results



Plots are saved automatically in the `results/` directory.



\## Project Structure



```

NREL-5MW-Analysis/

│

├── src/

│   └── nrel\_blade\_analysis.py

│

├── data/

│   └── blade\_definition.csv  (optional if you store raw tables)

│

├── results/

│   └── interpolated\_geometry.png

│   └── stiffness\_profile.png

│

├── README.md

├── requirements.txt

└── .gitignore

```



\## Meet the Author



\*\*Osama Abid\*\*

MSc Clean Energy Processes (FAU)

Mechanical Design Engineer interested in wind turbine design, computational tools, and renewable system optimisation.
www.linkedin.com/in/osama-abid



