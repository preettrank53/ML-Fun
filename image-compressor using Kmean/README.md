
# 📷 Image Compressor using KMeans

This is a simple web app that allows you to compress images using **KMeans clustering**. It automatically reshapes the image, determines the best number of clusters (`k`) using the Elbow method, and outputs a compressed image.

Built with:
- Python + Flask
- Scikit-learn (KMeans + Pipeline)
- Pillow (image processing)
- HTML/CSS (Frontend UI)

---

## 🚀 Features

- Upload any `.jpg`/`.png` image
- Automatically reshapes the image for clustering
- Chooses the best `k` (number of colors) using the Elbow method
- Displays and allows download of the compressed image
- Clean, responsive UI

---

## 🖥️ How to Run Locally

You can run this project using either `conda` or `venv`.

---

### 🐍 Using Conda

```bash
# Step 1: Create and activate environment
conda create -n image-kmeans-env python=3.10
conda activate image-kmeans-env

# Step 2: Install requirements
conda install flask numpy pillow scikit-learn joblib matplotlib

# Step 3: Run the app
python app.py
```

---

### 💡 Using pip / venv (no conda)

```bash
# Step 1: Create virtual environment
python -m venv venv
# Activate it
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Step 2: Install dependencies
pip install flask numpy pillow scikit-learn joblib matplotlib

# Step 3: Run the app
python app.py
```

---

## 📂 Project Structure

```
image-kmeans-app/
├── app.py
├── pipeline_creator.py
├── kmeans_pipeline.pkl
├── templates/
│   └── index.html
├── static/
│   └── compressed.jpg
├── uploads/
│   └── [uploaded files]
├── Screenshot.png
└── README.md
```

---

## 🖼️ Screenshot

![Screenshot](Screenshot%202025-07-12%20154739.png)

---

## ✅ What You Learn

- How to use `make_pipeline` and `KMeans` in a real-world app
- How to pickle and reuse pipelines using `joblib`
- How to reshape images and reduce colors using unsupervised learning
- How to integrate ML with a Flask web app

---

## 📜 License

This project is open-source and free to use under the MIT License.

---

## 🙌 Contribute

PRs and feedback welcome! Just fork the repo, make changes, and submit a pull request.

---
