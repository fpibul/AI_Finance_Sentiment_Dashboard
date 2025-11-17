import yfinance as yf

ticker = "TSLA"   # Change this to NVDA, MSFT, META later
stock = yf.Ticker(ticker)
news = stock.news

for article in news[:5]:
    if "title" in article:
        print(article["title"])
    else:
        print("Skipping article with no title...")
