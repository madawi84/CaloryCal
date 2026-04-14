# src/

This folder contains the core implementation of the **CaloryCal** pipeline.

The code in this directory transforms the experimental notebook into a modular and reusable system.

---

## 📌 Overview

The pipeline follows a multi-stage process:

```
Image → Segmentation → Depth → Portion Estimation → Calorie Estimation
```

Each stage is implemented as a separate module for clarity and maintainability.

---

## 📂 Modules

### 1. segmentation.py
Handles food detection and segmentation using a trained YOLO model.

**Input:**
- image path

**Output:**
- detected food items
- segmentation masks
- labels and confidence scores

---

### 2. depth.py
Handles depth estimation from the input image.

**Current state:**
- Uses a placeholder or Depth Anything V2 output

**Output:**
- depth map aligned with the input image

---

### 3. portion.py
Computes relative portion sizes for each detected food item.

**Key idea:**
Because depth is relative (not in centimetres), the system uses a **relative size score** based on:

- pixel area of the mask
- depth statistics (median / mean)

**Output:**
- size_score
- normalised size_score
- portion estimate (small / medium / large)

---

### 4. calories.py
Estimates calories using food label and relative portion size.

**Approach:**
- map each food label to a base calorie value
- scale calories using the relative portion size

**Formula:**
```
portion_scale = 0.5 + size_score_norm
estimated_calories = base_calories × portion_scale
```

---

### 5. pipeline.py
Combines all modules into a complete end-to-end pipeline.

**Steps:**
1. Load image  
2. Run segmentation  
3. Compute depth map  
4. Extract per-item features  
5. Estimate portion sizes  
6. Estimate calories  
7. Return final results  

---

## ⚠️ Important Notes

- The current system uses **relative size estimation**, not real-world measurements.
- Depth values are not calibrated to real units (cm or mm).
- Calorie estimation is therefore **relative**, not exact.

---

## 🚀 Future Improvements

- Replace relative depth with real-world scale (camera calibration or LiDAR)
- Integrate SAM for better segmentation boundaries
- Improve class mapping and food-specific calibration
- Use external nutrition databases (e.g., USDA API)

---

## 🧠 Summary

This folder represents the transition from:

Notebook prototype → Structured, reusable system

and is the foundation for future deployment (mobile or API-based).
