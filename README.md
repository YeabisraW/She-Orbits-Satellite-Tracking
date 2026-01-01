# 🛰️ She Orbits: Satellite Ground Tracking Project
**Researcher:** Yeabsira Wubishet Engda  
**Final Report:** January 2026

## 📜 Executive Summary
This project fulfills the one-month research assistantship plan for the **She Orbits** initiative. It provides a technical and educational framework for understanding satellite orbital mechanics through real-time data tracking of the International Space Station (ISS).

## ✅ Monthly Deliverables Tracker
| Week | Objective | Status | Key Output |
| :--- | :--- | :--- | :--- |
| **1** | Research & Repo Setup | Completed | TLE Glossary & Project Architecture |
| **2** | Data Acquisition | Completed | Automated CelesTrak TLE Fetching Script |
| **3** | Orbital Propagation | Completed | SGP4 Nadir Point Calculation & Dataset |
| **4** | Visualization & Reporting | Completed | ISS Ground Track Sinusoidal Map |

## 📊 Scientific Visualization
The following ground track was generated using my custom Python pipeline. It demonstrates the **Inclination** of the ISS and the effect of Earth's rotation on ground-track drift.

![ISS Ground Track](Media/iss_ground_track_plot.png)



## 🛠️ Technical Stack
- **Language:** Python 3.x
- **Libraries:** `skyfield` (SGP4), `pandas` (Data), `matplotlib` (Plotting)
- **Data Source:** CelesTrak GP (General Perturbations)

## 📂 Project Structure
- `01_Research/`: Deep-dive into TLE "Digital Passports."
- `02_Data/`: Python scripts for live tracking and CSV generation.
- `03_Tutorials/`: Plotting logic for future STEM cohorts.
- `Media/`: Exported orbital maps and diagrams.

---
*Submitted as the final requirement for the She Orbits Research Assistantship.*
