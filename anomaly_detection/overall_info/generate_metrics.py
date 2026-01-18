import json, yaml, random
from datetime import datetime, timedelta
from trace_chain import generate_trace_chain

# Load configs
topology = json.load(open("topology.json"))
cfg = yaml.safe_load(open("config_metrics.yaml"))

CPU = cfg["cpu"]
MEM = cfg["memory"]
LAT = cfg["latency"]
TP  = cfg["throughput"]

def gen_percent(conf, anomaly):
    if anomaly:
        return round(random.uniform(conf["anomaly_min"], conf["anomaly_max"]), 2)
    return round(random.uniform(conf["normal_min"], conf["normal_max"]), 2)

def generate_metrics(num_requests=300):
    rows = []
    current = datetime.now()

    for _ in range(num_requests):
        spans = generate_trace_chain(topology)
        anomaly = random.random() < 0.07  # anomaly theo trace chain

        for span in spans:
            service = span["service"]

            row = {
                "timestamp": current.isoformat(),
                "trace_id": span["trace_id"],
                "span_id": span["span_id"],
                "parent_span_id": span["parent_span_id"],
                "service": service,
                "cpu": gen_percent(CPU, anomaly),
                "memory": gen_percent(MEM, anomaly),
                "latency": gen_percent(LAT, anomaly),
                "throughput": random.randint(TP["normal_min"], TP["normal_max"]),
                "is_anomaly": anomaly
            }
            rows.append(row)
            current += timedelta(milliseconds=300)

    return rows

rows = generate_metrics()

with open("apm_metrics.jsonl", "w") as f:
    for r in rows:
        f.write(json.dumps(r) + "\n")

print("Metrics with full trace chain generated!")
