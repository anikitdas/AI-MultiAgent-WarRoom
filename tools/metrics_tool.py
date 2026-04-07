def analyze_metrics(file):
    with open(file, "r") as f:
        lines = f.readlines()

    headers = lines[0].strip().split(",")
    first = lines[1].strip().split(",")
    last = lines[-1].strip().split(",")

    trends = {}

    for i in range(1, len(headers)):
        if float(last[i]) < float(first[i]):
            trends[headers[i]] = "down"
        else:
            trends[headers[i]] = "up"

    print("[Metrics Tool] Trends:", trends)
    return trends