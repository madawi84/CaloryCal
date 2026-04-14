# 🍽️ CaloryCal

### AI-Based Food Calorie Estimation from a Single Image

---

## 📌 Overview

**CaloryCal** is an AI-powered system that estimates the caloric content of food from a single image. The system combines **instance segmentation**, **depth estimation**, and **nutritional modelling** to produce **per-item calorie estimates**, rather than treating the entire plate as a single unit.

The project has progressed beyond proof-of-concept and now demonstrates a **complete end-to-end pipeline**, with current limitations primarily related to **data quality and class imbalance**, not model capability.

---

## 🎯 Key Features

* 🍛 **Food Detection & Segmentation** using YOLO segmentation
* 📏 **Portion Size Estimation** using depth maps
* ⚖️ **Relative portion-based calorie estimation** using segmentation and depth
* 🧠 **Data-centric optimisation strategy** (handling long-tail distribution)
* 📱 **Planned mobile deployment (iPhone-first approach)**
* 🧩 **Future integration with SAM (Segment Anything Model)** for refinement

---

## 🏗️ System Pipeline

```
Input Image
     ↓
Food Segmentation (YOLO)
     ↓
Depth Estimation (Depth Anything V2)
     ↓
Mask Area + Depth Statistics Extraction
     ↓
Relative Portion Estimation (Size Score)
     ↓
Normalisation & Portion Classification (small / medium / large)
     ↓
Calorie Estimation (Base Calories × Portion Scale)
```

---

## 🧮 Calorie Estimation Model

The current system estimates calories using a **relative portion-based approach**, rather than true physical volume.

### Step 1 — Relative Size Score

A size score is computed for each food item using:

- pixel area of the segmentation mask  
- relative depth statistics (median or mean depth)

```
size_score = pixel_area × depth_median
```

---

### Step 2 — Normalisation

The size score is normalised across all detected items:

```
size_score_norm = size_score / max(size_score)
```

---

### Step 3 — Portion Classification

The normalised score is mapped to portion categories:

- small (< 0.33)  
- medium (< 0.66)  
- large (≥ 0.66)  

---

### Step 4 — Calorie Estimation

Each food item is assigned a base calorie value and scaled using the relative portion size:

```
portion_scale = 0.5 + size_score_norm
estimated_calories = base_calories × portion_scale
```
### Example Calorie Reference

The system uses a reference dictionary mapping food labels to base calorie values:

```
python
calorie_reference = {
    "rice": 206,
    "bread": 80,
    "tomato": 22,
    "chicken duck": 239,
    "pizza": 285,
    ...
}
```

Unknown items are assigned a default calorie value.
---

### ⚠️ Important

This approach provides **relative calorie estimates**, not exact real-world measurements.

True physical modelling (volume, density, calibrated depth) is planned as future work.


## 📊 Current Results

| Metric        | Value |
| ------------- | ----- |
| Box mAP50     | 0.376 |
| Box mAP50–95  | 0.316 |
| Mask mAP50    | 0.378 |
| Mask mAP50–95 | 0.301 |

### 🔍 Interpretation

* The model is **functionally stable**
* Performance is limited by **data quality**, not architecture
* Segmentation errors directly affect calorie estimation

---

## ⚠️ Key Challenges

* Long-tail class distribution (FoodSeg103 dataset)
* Visually ambiguous categories (e.g., sauces, mixed food)
* Label noise and segmentation boundary errors
* Class imbalance affecting rare food detection

---

## 🚀 Future Work & Roadmap

### Phase 1 — Data-Centric Optimisation

* Introduce **On-the-Fly Balanced Sampling**
* Reduce class space to high-impact food categories
* Improve annotation quality and dataset coverage

### Phase 2 — Inference Pipeline

* Build lightweight inference module
* Separate training from deployment

### Phase 3 — Mobile Deployment (iPhone First)

* Use **LiDAR / depth APIs**
* Enforce controlled capture:

  * Top-down image
  * Plate alignment zone
* Improve real-world reliability

### Phase 4 — Segmentation Refinement

* Integrate **SAM (Segment Anything Model)**
* Improve:

  * Boundary precision
  * Overlapping food separation

### Phase 5 — System Expansion

* Expand food categories
* Improve generalisation
* Replace proxy volume with **true geometric modelling**

---

## 📂 Project Structure

```
CaloryCal/
│
├── notebooks/              # Development notebooks            
├── src/                    # Core pipeline modules
├── models/                 # Trained weights
├── data/                   # Sample data & configs
├── results/                # Outputs & metrics
├── docs/                   # Proposal & documentation
└── README.md
```

---

## ⚙️ Installation

```bash
# Create environment
python -m venv env
source env/bin/activate  # or env\Scripts\activate on Windows

# Install dependencies
pip install -r requirements.txt
```

---

## ▶️ Usage

```python
from ultralytics import YOLO

# Load model
model = YOLO("models/best.pt")

# Run inference
results = model("data/sample.jpg")

# Visualise masks only
img = results[0].plot(boxes=False, labels=True, conf=False)
```

---

## 🧪 Technologies Used

* YOLO (Ultralytics) — segmentation
* Depth Anything V2 — depth estimation
* Python / PyTorch
* FoodSeg103 dataset

---

## 📖 Documentation

* Full proposal available in `/docs`
* Includes:

  * System architecture
  * Experimental results
  * Data-centric strategy
  * Implementation roadmap

---

## 💡 Research Contribution

CaloryCal demonstrates that:

> **The main bottleneck in food calorie estimation is not model complexity, but data quality and structure.**

The project adopts a **data-centric AI approach**, prioritising:

* Class balance
* Label quality
* Real-world deployment constraints

---

## 🧭 Future Vision

* Real-time mobile calorie estimation
* Integration with nutrition APIs (e.g., USDA)
* Personalised dietary tracking
* Clinical and healthcare applications

---

## 👤 Author

**Madawi Alsoyohi**
Data Scientist | Data Scientist

---

## ⭐ Final Note

This project is an evolving system designed to bridge **computer vision** and **nutritional intelligence**.
It is currently transitioning from a research prototype to a **deployable real-world solution**.

---
