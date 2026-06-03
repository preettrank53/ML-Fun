# ML-Fun

## Overview
ML-Fun is a curated portfolio of machine learning projects organized by domain. Each project is contained in its own directory with its notebooks, code, data assets, and supporting documentation.

## Project Index

### Classification
- **Fake Currency Detection**: Deep learning image classification for real vs. fake currency using MobileNetV2 transfer learning, two-branch embeddings, fine-tuning, and attention (CBAM).
  - Project: [classification/fake-currency-detection](classification/fake-currency-detection)
  - Key notebooks: [01_Base_Model_Training.ipynb](classification/fake-currency-detection/01_Base_Model_Training.ipynb), [02_Two_Branch_Model_Training.ipynb](classification/fake-currency-detection/02_Two_Branch_Model_Training.ipynb), [03_feature-enhancements.ipynb](classification/fake-currency-detection/03_feature-enhancements.ipynb), [04_attention-enhanced-model.ipynb](classification/fake-currency-detection/04_attention-enhanced-model.ipynb)
  - Models: [Models](classification/fake-currency-detection/Models)

### Natural Language Processing
- **News Article Summarizer with Sentiment Analysis**: Streamlit app that extracts article metadata, summarizes content, and classifies sentiment using standard NLP tooling.
  - Project: [nlp/news-article-summarizer-sentiment-analysis](nlp/news-article-summarizer-sentiment-analysis)
  - App entry point: [app.py](nlp/news-article-summarizer-sentiment-analysis/app.py)
  - Notebook: [Cleaned_News_Article_Summarizer.ipynb](nlp/news-article-summarizer-sentiment-analysis/Cleaned_News_Article_Summarizer.ipynb)
- **SMS Spam Detection**: TF-IDF based spam classifier with Streamlit UI and serialized model artifacts.
  - Project: [nlp/sms-spam-detection](nlp/sms-spam-detection)
  - App entry point: [app.py](nlp/sms-spam-detection/app.py)
  - Notebook: [SMS_spam_detection.ipynb](nlp/sms-spam-detection/SMS_spam_detection.ipynb)

### Clustering and Segmentation
- **Customer Segmentation using KMeans (RFM)**: Unsupervised clustering based on Recency, Frequency, and Monetary features with elbow and silhouette evaluation.
  - Project: [clustering/customer-segmentation-kmeans](clustering/customer-segmentation-kmeans)
  - Notebook: [customer-segmentation.ipynb](clustering/customer-segmentation-kmeans/customer-segmentation.ipynb)
  - Dataset output: [final_customer_segments_original_values.csv](clustering/customer-segmentation-kmeans/final_customer_segments_original_values.csv)
- **Image Compressor using KMeans**: Flask web app that compresses images via KMeans color clustering and a reusable pipeline.
  - Project: [clustering/image-compressor-kmeans](clustering/image-compressor-kmeans)
  - App entry point: [app.py](clustering/image-compressor-kmeans/app.py)
  - Notebook: [image_compressor.ipynb](clustering/image-compressor-kmeans/image_compressor.ipynb)

## Structure
```
ML-Fun/
  classification/
    fake-currency-detection/
  clustering/
    customer-segmentation-kmeans/
    image-compressor-kmeans/
  nlp/
    news-article-summarizer-sentiment-analysis/
    sms-spam-detection/
```
