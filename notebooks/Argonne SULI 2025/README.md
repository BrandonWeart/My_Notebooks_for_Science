# SULI 2025 - Argonne National Laboratory
## Mentor: Dr. Robert Jackson


This project explores the use of basic machine learning techniques to predict radar-derived rainfall.
(As well as various other side-assignments related to this as assigned by Bobby and others at ANL. Figure notebooks for papers as well.)
---

## Overview

Brief paragraph explaining:

- This project explores the use of basic machine learning techniques to predict radar-derived rainfall. The intention is to find a method that outperforms typical \n Z-R relationships.

- Radar-derived precipitation suffers from major biases due to poor representation of precipitation size distribution and indirect observation of actual hydrometeors. The Z-R relationships currently available eseentially cast a wide net to ***roughly*** cover all precip shapes and sizes, leaving much room for error in precipitation estimation. It is possible that a data-driven approach using simple machine learning models could provide a more tailored Z-R relationship on an event basis, which would enable better radar-derived precipitation estimation.
- Community Research on Climate and Urban Science (CROCUS) field campaign data from individual observation nodes, along with NEXRAD data from KLOT radar are used in this project.
- This folder also includes other exploratory branches taken by me during the project to just mess with machine learning, computer vision, radar files, and to make figures all from the same type of data. Heavy use of NetCDF, GRIB, as well as some use of MetPy for deriving specific parameters such as Theta-E and convergence and working with units and other calculations.

- During this internship, I was tasked with creating figures for two BAMS papers (Currently in review), which I have included the notebooks for in the BAMS figure subfolder of the repo.


## Folder Contents

- `/BAMS Figures` — Two notebooks showing BAMS figures I made for *Collis et al.* (2026) and *Muradyan et al.* (2026).
- `/Field Campaign Analysis` — Analysis of wind sonde and radiosonde data from the Urban Canyons field campaign. Some figures may also appear in *Collis et al.* (2026).
- `/Lake Breeze CV Stuff` — Notebook with HRRR lake-breeze detection using basic computer vision techniques on convergence (MetPy used).
- `/Main Project (Simple ML stuff)` — Notebooks exploring linear regression and shallow neural networks to predict radar-derived precipitation.
- `/Radar Vertical Column` — Notebook using Py-ART to explore radar vertical column extraction and feature detection.
- `/Side Projects During Internship` — Notebook using Herbie and MetPy to plot Theta-E from HRRR data.

### SULI Internship Deliverables

- Paper (`Weart-Brandon-SULI-EVS-Paper.pdf`)
- Poster (`Weart-Brandon-SULI-EVS_Final_Poster.pdf`)
- General-audience abstract (`General Audience Abstract.pdf`)


--------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Enjoy!
---

