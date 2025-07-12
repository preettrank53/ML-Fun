# pipeline_creator.py
from sklearn.pipeline import make_pipeline
from sklearn.cluster import KMeans
import joblib

# Save a generic pipeline with k=1 (placeholder)
pipeline = make_pipeline(KMeans(n_clusters=1))  # placeholder
joblib.dump(pipeline, 'kmeans_pipeline.pkl')
print("✅ Pipeline template saved to kmeans_pipeline.pkl")
