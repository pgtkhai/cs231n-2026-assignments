# CS231n: Deep Learning for Computer Vision (2026)

This repository contains implementations, solutions, and notes for the assignments in **Stanford University's CS231n: Deep Learning for Computer Vision** course.

---

## Repository Overview

The course covers computer vision fundamentals, deep learning architectures, optimization, neural network training techniques, and state-of-the-art vision models.

```
CS231N - Deep Learning for Computer Vision/
├── assignment1/    # k-NN, SVM, Softmax, Two-Layer Neural Net, Image Features
├── assignment2/    # Fully-Connected Nets, Batch Normalization, Dropout, CNNs, PyTorch, RNN Captioning
└── assignment3/    # Transformers, Self-Supervised Learning (SimCLR), Diffusion Models (DDPM), CLIP & DINO
```

---

## Assignment Breakdown

### [Assignment 1](assignment1/)
- **k-Nearest Neighbor (k-NN)** classifier.
- **Multiclass Support Vector Machine (SVM)** classifier.
- **Softmax** classifier with cross-entropy loss.
- **Two-Layer Neural Network** implemented from scratch in NumPy.
- **Higher-level Image Features** (HOG & Color Histograms).

### [Assignment 2](assignment2/)
- **Fully-Connected Neural Networks** with modular layer architecture.
- **Batch Normalization** (forward and backward passes).
- **Dropout** for regularization.
- **Convolutional Neural Networks (CNNs)** from scratch.
- **PyTorch** deep learning framework introduction.
- **Image Captioning** using Recurrent Neural Networks (RNNs).

### [Assignment 3](assignment3/)
- **Transformer** architectures for Image Captioning.
- **Self-Supervised Learning** using SimCLR.
- **Denoising Diffusion Probabilistic Models (DDPM)**.
- **Vision-Language & Foundation Models** (CLIP & DINO).

---

## Environment Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/cs231n-2026-assignments.git
   cd cs231n-2026-assignments
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv .venv
   # On Windows (PowerShell):
   .\.venv\Scripts\Activate.ps1
   # On macOS/Linux:
   source .venv/bin/activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Datasets:**
   Navigate into each assignment's dataset directory to fetch required data:
   ```bash
   cd assignment1/cs231n/datasets
   bash get_datasets.sh
   ```

---

## Academic Integrity & Honor Code

This repository is maintained for personal learning, revision, and portfolio purposes. 

If you are a student currently taking Stanford's CS231n course (or an equivalent course using these assignments), please adhere to your institution's Honor Code. Do not copy or plagiarize solutions from this repository.

---