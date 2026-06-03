# News Article Summarizer with Sentiment Analysis

A Streamlit-based application that extracts metadata from a news article URL, generates a concise summary, and performs sentiment analysis using standard NLP libraries.

## Overview

Provide a news article URL and the application will:

- Extract the article title, authors, and publish date
- Generate a summary of the article content
- Classify sentiment as **Positive**, **Neutral**, or **Negative**

## Live Demo

A hosted demo is not currently available. Run the application locally using the instructions below.

## Key Features

- **Summary generation** using `newspaper3k`
- **Sentiment analysis** using `TextBlob`
- **Streamlit UI** for interactive usage
- **403 handling** via randomized user-agent headers (to improve extraction reliability)

## Requirements

- Python 3.7+
- `streamlit`
- `nltk`
- `newspaper3k`
- `textblob`

## Installation and Setup

### Option 1: Virtual Environment (`venv`)

```bash
# 1. Clone the repository
git clone https://github.com/preettrank53/News-Article-Summarizer-with-Sentiment-Analysis.git
cd news-summarizer

# 2. Create a virtual environment
python -m venv env

# 3. Activate the virtual environment
# Windows:
env\Scripts\activate
# macOS/Linux:
source env/bin/activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Run the app
streamlit run app.py
```

### Option 2: Conda (Recommended)

```bash
# 1. Clone the repository
git clone https://github.com/preettrank53/News-Article-Summarizer-with-Sentiment-Analysis.git
cd news-summarizer

# 2. Create and activate conda environment
conda create -p venv python=3.10
conda activate venv/

# 3. Install dependencies
pip install -r requirements.txt

# 4. Run the app
streamlit run app.py
```
