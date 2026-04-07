def risk_agent(metrics, sentiment):
    print("[Risk Agent] Identifying risks...")

    risks = []

    if metrics.get("crash_rate") == "up":
        risks.append("High crash rate increasing")

    if sentiment["negative"] > sentiment["positive"]:
        risks.append("User dissatisfaction rising")

    return risks