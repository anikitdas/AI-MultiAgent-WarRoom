def data_agent(metrics):
    print("[Data Agent] Checking metrics...")

    issues = [k for k, v in metrics.items() if v == "down"]
    return f"Declining metrics: {issues}"