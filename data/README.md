# data/

This folder contains sample data and configuration files required to run and test **CaloryCal**.

---

## 📂 Structure

```
data/
├── sample_images/
│   └── test.jpg
├── configs/
│   ├── dataset.yaml
│   └── arges.yaml
```

---

## 📸 sample_images/

Contains example images used for inference and testing.

### Example
- `test.jpg` — sample food image used to run the full pipeline:
  - segmentation
  - depth estimation
  - portion estimation
  - calorie estimation

---

## ⚙️ configs/

Contains configuration files used during training and experimentation.

### dataset.yaml
Used by YOLO for training and validation.

Defines:
- dataset paths (train / val)
- class names

This file is required when training the segmentation model.

---

### arges.yaml
Contains training arguments and experiment configuration.

Typical contents may include:
- batch size
- number of epochs
- image size
- training settings

This file is used to control training behaviour but does not define dataset structure.

---

## ⚠️ Notes

- The full dataset (FoodSeg103) is **not included** due to size.
- Only a small sample image is provided for demonstration and testing.
- To train the model, users must download the dataset separately.
- The current system uses **relative portion estimation**, not real-world measurements.

---

## 🧠 Summary

This folder provides:
- a minimal test image for running the pipeline
- configuration files for training and experimentation

It allows the project to be runnable without requiring the full dataset.
