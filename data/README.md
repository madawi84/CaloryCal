# data/

This folder contains sample data and configuration files for running **CaloryCal**.

---

## 📂 Structure

```
data/
├── sample_images/
│   └── test.jpg
├── configs/
│   └── dataset.yaml
```

---

## 📸 sample_images/

Contains example images used for testing the pipeline.

### Example
- `test.jpg` — sample food image used for inference

---

## ⚙️ configs/

Contains dataset configuration files used during training.

### dataset.yaml
Defines:
- dataset paths
- class names

---

## ⚠️ Notes

- The full dataset (FoodSeg103) is **not included** due to size.
- Only small sample images are provided for testing.
- Users should download the full dataset separately if training is required.
