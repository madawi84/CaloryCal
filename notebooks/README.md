## notebooks/

This folder contains the main Google Colab notebook used to develop, test, and validate the **CaloryCal** prototype.

### File
- `CaloryCal_pipeline.ipynb`

### What this notebook includes
The notebook documents the full experimental workflow of the project, including:

- environment setup and package installation
- dataset loading and inspection
- FoodSeg103 mask exploration and visualisation
- class balance analysis
- conversion of FoodSeg103 masks into YOLO segmentation labels
- training data oversampling for rare classes
- YOLO segmentation training and validation
- prediction on sample food images
- depth estimation experiments
- extraction of mask area and depth statistics per food item
- calorie estimation workflow
- result visualisation and export

### Purpose
This notebook represents the **research and prototyping stage** of the project. It was used to build the end-to-end pipeline before modularising the system into reusable scripts inside the `src/` folder.

### Notes
- Keep only **one clean final notebook** in this folder.
- Remove failed experiments, duplicate cells, and unnecessary outputs before uploading to GitHub.
- Keep important visual outputs that demonstrate segmentation, depth estimation, and calorie estimation results.
