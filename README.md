# AI Multi-Agent War Room System

## Overview
This project implements a multi-agent system that simulates a product launch war room.  
It analyzes metrics, user feedback, and release notes to generate a launch decision:
**Proceed / Pause / Rollback**.

---

## Agents
- Product Manager Agent
- Data Analyst Agent
- Marketing Agent
- Risk/Critic Agent
- Support Agent

---

## Tools
- Metrics Analysis Tool
- Sentiment Analysis Tool

---

## Input Data
- Metrics (CSV file with trends)
- User feedback (25 entries)
- Release notes

---

## Output
The system generates:

### launch_decision_output.json
- Decision
- Rationale
- Risk register
- Action plan (24–48 hours)
- Communication plan
- Confidence score

### trace_log.txt
- Logs of agent steps and tool outputs

---

## Run

```bash
python main.py
