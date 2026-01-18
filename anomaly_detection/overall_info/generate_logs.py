import json, yaml, random, uuid
from datetime import datetime, timedelta
from trace_chain import generate_trace_chain

topology = json.load(open("topology.json"))
cfg = yaml.safe_load(open("config_logs.yaml"))

LEVEL_PROB = cfg["log_levels"]
PATHS       = cfg["paths"]
MESSAGES    = cfg["messages"]
STATUS      = cfg["status_code"]
LAT         = cfg["latency"]

def pick_prob(p):
    r = random.random()
    cum = 0
    for k, v in p.items():
        cum += v
        if r <= cum:
            return k
    return list(p.keys())[-1]

def generate_logs(num_requests=300):
    out = []
    now = datetime.now()

    for _ in range(num_requests):
        spans = generate_trace_chain(topology)

        anomaly = random.random() < 0.07

        for span in spans:
            svc = span["service"]
            level = pick_prob(LEVEL_PROB)

            latency = random.uniform(
                LAT["anomaly_min"], LAT["anomaly_max"]
            ) if anomaly else random.uniform(
                LAT["normal_min"], LAT["normal_max"]
            )

            entry = {
                "timestamp": now.isoformat(),
                "trace_id": span["trace_id"],
                "span_id": span["span_id"],
                "parent_span_id": span["parent_span_id"],
                "service": svc,
                "level": level,
                "path": random.choice(PATHS[svc]),
                "message": random.choice(MESSAGES[level]),
                "status": random.choice(STATUS[level]),
                "latency_ms": round(latency, 2),
                "is_anomaly": anomaly
            }

            out.append(entry)
            now += timedelta(milliseconds=random.randint(50, 250))

    return out

logs = generate_logs()

with open("application_logs.jsonl", "w") as f:
    for l in logs:
        f.write(json.dumps(l) + "\n")

print("Application logs with trace chain generated!")
