import matplotlib.pyplot as plt
import streamlit as st
import requests
from transformers import pipeline

API_KEY = "5057b417919f4bee92e19f2f4b1255ab"   # <--- insert your key

st.title("AI Financial News Sentiment Analyzer")

query = st.text_input("Enter a stock, company, or keyword:", "Tesla")

if st.button("Analyze"):
    # Step 1: Get news
    url = (
        "https://newsapi.org/v2/everything?"
        f"q={query}&"
        "sortBy=publishedAt&"
        "language=en&"
        f"apiKey={API_KEY}"
    )

    response = requests.get(url).json()
    articles = response.get("articles", [])[:5]

    # Step 2: Load AI sentiment model
    sentiment_model = pipeline("sentiment-analysis")

    st.header("Results:")

    positive_count = 0
    negative_count = 0

    # Step 3: Analyze sentiment
    for article in articles:
        title = article.get("title", "No title")
        result = sentiment_model(title)[0]
        label = result["label"]

        if label == "POSITIVE":
            positive_count += 1
        else:
            negative_count += 1

        st.subheader(title)
        st.write(f"**Sentiment:** {label} (confidence {round(result['score'], 3)})")
        st.write("---")

    # Step 4: Summary section
    st.header("Overall Sentiment Summary")
    st.write(f"Positive Articles: {positive_count}")
    st.write(f"Negative Articles: {negative_count}")

    # Step 5: Pie chart
    labels = ['Positive', 'Negative']
    sizes = [positive_count, negative_count]
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    st.pyplot(fig)
