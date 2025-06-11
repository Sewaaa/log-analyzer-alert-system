import yaml
from collections import defaultdict
from datetime import datetime

def load_rules(yaml_path):
    # Load anomaly detection rules from a YAML file.
    with open(yaml_path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["rules"]

def parse_time(ts):
    # Parse a timestamp string in the format 'Mon DD HH:MM:SS' to a datetime object.
    return datetime.strptime(ts, "%b %d %H:%M:%S")

def detect_anomalies(events, rules):
    # Detect anomalies in a list of events based on a set of rules.
    alerts = []

    # Iterate over each rule and apply it to the events
    for rule in rules:
        pattern = rule["pattern"]       
        field = rule["field"]           
        threshold = rule["threshold"]  
        interval = rule["interval"]     

        # Group events by the specified field if they match the rule pattern
        grouped = defaultdict(list)
        for event in events:
            if event["event"] == pattern:
                grouped[event[field]].append(event)

        # Check each group of events for threshold matches within the time interval
        for key, evts in grouped.items():
            times = [parse_time(e["timestamp"]) for e in evts]
            times.sort()

            for i in range(len(times)):
                # Create a window of 'threshold' events
                window = times[i : i + threshold]
                if len(window) == threshold and (window[-1] - window[0]).total_seconds() <= interval:
                    alerts.append({
                        "rule_id": rule["id"],
                        "description": rule["description"],
                        "offender": key,
                        "count": threshold,
                        "time_window_start": window[0].strftime("%H:%M:%S"),
                        "time_window_end": window[-1].strftime("%H:%M:%S")
                    })
                    break  # Stop after the first valid window is found

    return alerts
