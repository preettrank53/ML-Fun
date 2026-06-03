import streamlit as st
import nltk
from newspaper import Article
from textblob import TextBlob
import random

# Download NLTK tokenizer
nltk.download('punkt')

# Fake browser user agents to avoid 403 errors
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
]

# Function to get article with headers
def get_article_with_headers(url):
    article = Article(url, browser_user_agent=random.choice(USER_AGENTS))
    article.download()
    article.parse()
    article.nlp()
    return article

# Streamlit app
st.set_page_config(page_title="News Summarizer & Sentiment", layout="centered")
st.title("📰 News Article Summarizer + Sentiment Analysis")

url = st.text_input("🔗 Enter a news article URL")

if st.button("Summarize and Analyze"):
    if url:
        try:
            article = get_article_with_headers(url)

            # Sentiment analysis
            analysis = TextBlob(article.text)
            polarity = analysis.sentiment.polarity
            subjectivity = analysis.sentiment.subjectivity

            # Display info
            st.subheader("📝 Title")
            st.write(article.title or "Not available")

            st.subheader("✍️ Author(s)")
            st.write(", ".join(article.authors) if article.authors else "Not available")


            st.subheader("📅 Published Date")
            st.write(str(article.publish_date) if article.publish_date else "Not available")

            st.subheader("📰 Summary")
            st.write(article.summary or "Summary could not be extracted.")

            st.subheader("📊 Sentiment Analysis")
            st.write(f"**Polarity**: `{polarity}`")
            st.write(f"**Subjectivity**: `{subjectivity}`")

            if polarity > 0:
                st.success("Overall Sentiment: Positive 😊")
            elif polarity < 0:
                st.error("Overall Sentiment: Negative 😞")
            else:
                st.info("Overall Sentiment: Neutral 😐")

        except Exception as e:
            st.error(f"⚠️ Something went wrong while processing the article: {e}")
    else:
        st.warning("⚠️ Please enter a valid URL.")
