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
* ⚖️ **Volume → Mass → Calories conversion pipeline**
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
Mask Area + Depth Extraction
     ↓
Volume Estimation (L × W × D)
     ↓
Mass Calculation (Volume × Density)
     ↓
Calories (Mass × Calories per gram)
```

---

## 🧮 Calorie Estimation Model

The system estimates calories using a physically interpretable pipeline:

* **Volume** = L × W × D
* **Mass (g)** = Volume × Density
* **Calories** = Mass × Calories per gram

A reference dictionary is used:

```python
food_db = {
    "rice": {"density": 0.9, "cal_per_g": 1.3},
    "chicken": {"density": 1.1, "cal_per_g": 2.4},
}
```

> ⚠️ Current implementation uses relative scaling. Future work will improve **true physical calibration**.

---

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
