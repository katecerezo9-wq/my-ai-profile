# 🧑‍💻 Personal Developer Profile & AI/Image Transformation App

Welcome to my personal portfolio repository! This project showcases a fully functional Python application that executes image processing and matrix transformations via code, tracked cleanly using `.git` version control.

## 🚀 App Capabilities
This program utilizes the **Pillow (PIL)** library to manipulate images:
1. **Grayscale Conversion:** Reduces RGB pixel matrices into a single 8-bit luminance channel.
2. **Gaussian Blur:** Applies a convolution matrix to smooth high-frequency spatial changes.
3. **Edge Detection:** Implements high-pass spatial filtering to locate steep color gradient boundaries.

---

## 🛠️ Code Architecture & Efficiency
* **Library Used:** `Pillow` (Highly efficient, industry-standard Python image manipulation toolkit).
* **Error Handling:** Features complete `try-except` blocks ensuring the system never crashes on missing assets.

---

## 📊 Visual Outputs & Explanations

| Original Input | Grayscale Transformation | Gaussian Blur Filter | Edge Detection Matrix |
| :---: | :---: | :---: | :---: |
| Place original image here | ![Grayscale](./outputs/transformed_grayscale.png) | ![Blur](./outputs/transformed_blurred.png) | ![Edges](./outputs/transformed_edges.png) |