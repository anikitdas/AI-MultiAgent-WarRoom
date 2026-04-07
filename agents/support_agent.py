def support_agent(sentiment):
    print("[Support Agent] Reviewing support load...")

    if sentiment["negative"] > 5:
        return "High support tickets expected"

    return "Normal support load"