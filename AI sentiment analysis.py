from textblob import TextBlob


def analyze_sentiment(text):

    blob = TextBlob(text)
    return blob.sentiment.polarity


def main():
    print("simple sentiment analysis using TextBlob")
    user_input = input("enter a sentence or text to analyze: ")

    polarity = analyze_sentiment(user_input)

    if polarity > 0:
        sentiment = "positive"
    elif polarity < 0:
        sentiment = "negative"
    else:
        sentiment = "neutral"

    print("\nanalysis Result:")
    print(f"text: {user_input}")
    print(f"sentiment: {sentiment} (polarity: {polarity:.2f})")


if __name__ == "__main__":
    main()
