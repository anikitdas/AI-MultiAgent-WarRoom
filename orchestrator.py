from tools.metrics_tool import analyze_metrics
from tools.sentiment_tool import analyze_sentiment

from agents.pm_agent import pm_agent
from agents.data_agent import data_agent
from agents.marketing_agent import marketing_agent
from agents.risk_agent import risk_agent
from agents.support_agent import support_agent

import json
from datetime import datetime

# =========================
# TRACE SETUP
# =========================
TRACE_FILE = "trace_log.txt"

def log_trace(message):
    with open(TRACE_FILE, "a") as f:
        f.write(message + "\n")


def run_system():
    print("\n--- SYSTEM START ---\n")

    # Clear old trace
    open(TRACE_FILE, "w").close()
    log_trace("=== NEW RUN STARTED ===")

    # =========================
    # STEP 1: LOAD INPUTS
    # =========================
    metrics = analyze_metrics("data/metrics.csv")
    sentiment = analyze_sentiment("data/feedback.txt")

    # Load release notes (IMPORTANT requirement)
    with open("data/release_notes.txt", "r") as f:
        release_notes = f.read()

    log_trace("Metrics analyzed: " + str(metrics))
    log_trace("Sentiment analyzed: " + str(sentiment))
    log_trace("Release Notes: " + release_notes)

    print("\n--- AGENT EXECUTION ---\n")

    # =========================
    # STEP 2: AGENT EXECUTION
    # =========================
    pm = pm_agent(metrics, sentiment)
    data = data_agent(metrics)
    marketing = marketing_agent(sentiment)
    risks = risk_agent(metrics, sentiment)
    support = support_agent(sentiment)

    log_trace("PM Agent Output: " + pm)
    log_trace("Data Agent Output: " + data)
    log_trace("Marketing Agent Output: " + marketing)
    log_trace("Risk Agent Output: " + str(risks))
    log_trace("Support Agent Output: " + support)

    print("\n--- DECISION ENGINE ---\n")

    # =========================
    # STEP 3: DECISION LOGIC
    # =========================
    if "High crash rate increasing" in risks:
        decision = "Rollback"
        confidence = 0.9
        confidence_reason = "Critical crash rate increase detected from metrics and supported by negative feedback"

    elif sentiment["negative"] > sentiment["positive"]:
        decision = "Pause"
        confidence = 0.7
        confidence_reason = "Negative user sentiment outweighs positive signals"

    else:
        decision = "Proceed"
        confidence = 0.85
        confidence_reason = "Stable metrics and positive user experience"

    log_trace("Final Decision: " + decision)
    log_trace("Confidence: " + str(confidence))

    print(f"Decision: {decision}")

    # =========================
    # STEP 4: STRUCTURED OUTPUT
    # =========================
    output = {
        "timestamp": str(datetime.now()),

        "decision": decision,

        "rationale": {
            "product_manager": pm,
            "data_analysis": data,
            "marketing": marketing,
            "support": support,
            "release_notes_context": release_notes
        },

        "risk_register": [
            {
                "risk": r,
                "severity": "high",
                "mitigation": "Immediate investigation and fix required"
            }
            for r in risks
        ],

        "action_plan_24_48h": [
            {
                "action": "Fix crash issues",
                "owner": "Engineering Team"
            },
            {
                "action": "Reduce API latency",
                "owner": "Backend Team"
            },
            {
                "action": "Stabilize payment system",
                "owner": "Payments Team"
            }
        ],

        "communication_plan": {
            "internal": "Immediately notify product, engineering, and leadership teams",
            "external": "Inform users about known issues and expected resolution timeline"
        },

        "confidence_score": confidence,
        "confidence_reason": confidence_reason
    }

    # =========================
    # STEP 5: SAVE OUTPUT
    # =========================
    with open("launch_decision_output.json", "w") as f:
        json.dump(output, f, indent=4)

    print("\n--- FINAL OUTPUT ---\n")
    print(json.dumps(output, indent=4))

    print("\n--- TRACE COMPLETE ---\n")