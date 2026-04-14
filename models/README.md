## models/

This folder contains the trained model weights used by **CaloryCal**.

### Files
- `best.pt` — best saved YOLO segmentation model from training

### Purpose
The model file is used for:
- food detection
- food segmentation
- label prediction during inference

### Notes
- `best.pt` is the main model used in the current prototype.
- Additional model files such as `last.pt` may be kept for experiment tracking, but `best.pt` is the recommended file for inference and evaluation.
- If the model file is too large for normal Git tracking, use **Git LFS** or provide a download link.
