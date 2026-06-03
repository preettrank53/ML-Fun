# Image Compressor using K-Means

This project is a simple web application that compresses images using K-Means clustering. It reshapes the image data, selects an appropriate number of clusters (`k`) using the Elbow Method, and produces a compressed output image.

Built with:
- Python + Flask
- scikit-learn (KMeans + Pipeline)
- Pillow (image processing)
- HTML/CSS (frontend UI)

## Features

- Upload `.jpg` / `.png` images
- Automatically reshapes images for clustering
- Selects `k` (number of colors) using the Elbow Method
- Displays the compressed image and allows downloading
- Clean, responsive UI

## How to run locally

You can run this project using either `conda` or `venv`.

### Using conda

```bash
# Step 1: Create and activate environment
conda create -n image-kmeans-env python=3.10
conda activate image-kmeans-env

# Step 2: Install requirements
conda install flask numpy pillow scikit-learn joblib matplotlib

# Step 3: Run the app
python app.py
```

### Using pip / venv (no conda)

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

## Project structure

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

## Screenshot

<img width="1872" height="850" alt="Screenshot" src="https://github.com/user-attachments/assets/e4cedacc-d635-4082-be77-425a8aaf3cb2" />

## What you learn

- Using `make_pipeline` and `KMeans` in an end-to-end application
- Saving and loading pipelines with `joblib`
- Reshaping images and reducing colors with unsupervised learning
- Integrating an ML pipeline into a Flask web application

## License

This project is open source under the MIT License.

## Contributing

Contributions are welcome. Fork the repository, make your changes, and open a pull request.
