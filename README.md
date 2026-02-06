♻️ Garbage Classification System

A deep learning–based image classification project that categorizes waste into classes such as Cardboard, Glass, Metal, Paper, Plastic, and Trash using transfer learning with MobileNetV3Large.

The primary focus of this project is building and evaluating an accurate image classification model, along with exploring deployment using Streamlit.

---

### Features
- Built using TensorFlow and Keras
- Transfer learning with MobileNetV3Large pretrained on ImageNet
- Image preprocessing and normalization pipeline
- Multi-class classification of common waste categories
- Streamlit-based interface for interactive image inference (experimental)

---

### Classes
The model is trained to identify the following categories:
- Cardboard
- Glass
- Metal
- Paper
- Plastic
- Trash

---

### Model Architecture
- Base model: MobileNetV3Large (ImageNet pretrained)
- Input shape: 224 × 224 × 3
- Fine-tuned classification head
- Accuracy achieved during local evaluation: **94.38%**

---

### Tech Stack
- TensorFlow, Keras
- NumPy, Pandas
- Streamlit
