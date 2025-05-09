﻿# CubicInsight-SplineSolver

## 🔷 Q1: Cubic Spline Interpolation & Data Visualization

📁 **Input:** Data from the file `bps.data`

### ✅ Task Breakdown

1. **Interpolation using Cubic Spline Method**  
   - Applied the **Cubic Spline Interpolation** method to approximate unknown values between known data points.  
   - Ensures continuity and smoothness (twice-differentiable) across intervals.  
   - Implemented both manually and via `scipy.interpolate.CubicSpline` in Python.

2. **Graphical Plot of the Data**  
   - Plotted:
     - The **original data points**.
     - The **cubic spline curve** fitting those points.  
   - Libraries: `matplotlib` for plotting, `numpy` for numerical operations.

### 📊 Sample Output

- Smooth, visually intuitive graph showing the spline curve and data points.
- Ideal for trend analysis and mid‐point predictions.

---
![image](https://github.com/user-attachments/assets/0042b6e9-f6cd-40af-9ca6-53397f7cd899)


## 🔷 Q2: Symbolic Solution of a System of Equations

Tackled a **non‑linear** system in `x`, `y`, and `z`:

### ✅ Task Breakdown

1. **Symbolic Computation with `sympy`**  
   - Defined each equation symbolically.  
   - Solved the three simultaneously for `x`, `y`, and `z`.  
   - Computed the derivative w.r.t. `r` for the third equation.

2. **Output**  
   - Explicit symbolic formulas for `x`, `y`, and `z`.

### 💡 Use Cases

Useful in physics or engineering when analytical insight into variable dependencies is required.

---
![image](https://github.com/user-attachments/assets/47f3562c-8453-4d42-ae63-5121e0bafd30)
![image](https://github.com/user-attachments/assets/a8a1c8b8-3324-47ff-8536-e82c3b8588c6)




## 🔷 Q3: Population Estimation using Newton’s Backward Interpolation

### 🏙️ Problem Statement

Estimate the **population increase** between **1976 and 1978** from census data.

### ✅ Task Breakdown

1. **Newton’s Backward Interpolation**  
   - Ideal for points near the end of the dataset.  
   - Builds on backward finite differences to predict unlisted values.

2. **Dynamic Year Estimation**  
   - Generic function to estimate population for **any year** within range.  
   - Implemented in both C++ and Python.

3. **Result**  
   - Estimated populations for 1976 & 1978.  
   - Computed the **increase** over that period.

![image](https://github.com/user-attachments/assets/33ca6bb2-e56e-4dea-b25d-f50d6ec943da)




