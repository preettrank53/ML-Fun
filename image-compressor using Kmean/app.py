from flask import Flask, render_template, request, send_from_directory
import os
from PIL import Image
import numpy as np
import joblib
from sklearn.cluster import KMeans
from sklearn.pipeline import Pipeline

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['STATIC_FOLDER'] = 'static'

# Load base pipeline once (optional if you want to use it)
base_pipeline = joblib.load("kmeans_pipeline.pkl")

def find_best_k(pixels, max_k=15):
    distortions = []
    K = range(2, max_k + 1)

    for k in K:
        kmeans = KMeans(n_clusters=k, random_state=42)
        kmeans.fit(pixels)
        distortions.append(kmeans.inertia_)

    distortions = np.array(distortions)
    second_derivative = np.diff(distortions, 2)

    if len(second_derivative) > 0:
        best_k = np.argmax(-second_derivative) + 3  # +3 due to diff twice and starting at k=2
    else:
        best_k = 3  # fallback

    # Optional: clamp k between reasonable range
    best_k = max(4, min(best_k, 12))

    print("Distortions:", distortions)
    print("Second Derivative:", second_derivative)
    print("Selected Best K:", best_k)

    return best_k

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['image']
        img_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(img_path)

        img = Image.open(img_path)
        img_np = np.array(img)
        original_shape = img_np.shape
        pixels = img_np.reshape(-1, 3)

        # Step 1: Find best k
        best_k = find_best_k(pixels)

        # Step 2: Fit KMeans
        new_kmeans = KMeans(n_clusters=best_k, random_state=42)
        pipeline = Pipeline(steps=[('kmeans', new_kmeans)])
        pipeline.fit(pixels)

        kmeans = pipeline.named_steps['kmeans']
        new_colors = kmeans.cluster_centers_[kmeans.labels_].astype('uint8')
        compressed_img = new_colors.reshape(original_shape)

        # Save compressed image
        compressed_img_path = os.path.join(app.config['STATIC_FOLDER'], 'compressed.jpg')
        Image.fromarray(compressed_img).save(compressed_img_path)

        return render_template('index.html',
                               original_img=file.filename,
                               compressed_img='compressed.jpg',
                               best_k=best_k)

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == "__main__":
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('static'):
        os.makedirs('static')

    print("\nApp running! Open http://127.0.0.1:5000/ in your browser.\n")
    app.run(debug=True, host="0.0.0.0", port=5000)
