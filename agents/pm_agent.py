def pm_agent(metrics, sentiment):
    print("[PM Agent] Evaluating user impact...")

    if sentiment["negative"] > sentiment["positive"]:
        return "User experience degrading"

    return "User experience stable"