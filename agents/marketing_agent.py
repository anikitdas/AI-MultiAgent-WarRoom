def marketing_agent(sentiment):
    print("[Marketing Agent] Analyzing perception...")

    if sentiment["negative"] > sentiment["positive"]:
        return "Negative sentiment"

    return "Positive sentiment"