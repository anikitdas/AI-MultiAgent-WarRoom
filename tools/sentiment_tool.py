def analyze_sentiment(file):
    with open(file, "r") as f:
        lines = f.readlines()

    positive = 0
    negative = 0

    for line in lines:
        l = line.lower()

        if any(word in l for word in ["good", "great", "excellent", "love", "amazing"]):
            positive += 1

        if any(word in l for word in ["fail", "crash", "bug", "terrible", "slow", "lag"]):
            negative += 1

    result = {
        "positive": positive,
        "negative": negative,
        "total": len(lines)
    }

    print("[Sentiment Tool]:", result)
    return result