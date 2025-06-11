# Script to populate alert dashboard charts with synthetic data

import random
from datetime import datetime, timedelta
from elasticsearch import Elasticsearch

# Connect to Elasticsearch
es = Elasticsearch("http://127.0.0.1:9200", verify_certs=False)

INDEX = "log_analyzer_alerts"

# Static rule configuration
RULE_ID = "ssh_bruteforce"
DESCRIPTION = "More than 5 failed logins from the same IP within 30 seconds"
WINDOW_START = "12:45:32"
WINDOW_END   = "12:45:40"

# List of IPs simulating different offenders
OFFENDERS = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12",
    "192.168.1.13",
    "192.168.1.14"
]

def random_timestamp_for_day(day: datetime):
    """Returns a random ISO timestamp within the given day."""
    start = datetime(day.year, day.month, day.day, 0, 0, 0)
    end = start + timedelta(days=1)
    return (start + (end - start) * random.random()).isoformat()

def main():
    DAYS = 180
    today = datetime.utcnow().date()

    total = 0
    for delta in range(DAYS):
        day = today - timedelta(days=delta)
        # Number of alerts to generate for the given day (0-5)
        count = random.randint(0, 5)
        for _ in range(count):
            # Pick a random offender from the list
            offender = random.choice(OFFENDERS)
            doc = {
                "rule_id": RULE_ID,
                "description": DESCRIPTION,
                "offender": offender,
                "time_window_start": WINDOW_START,
                "time_window_end": WINDOW_END,
                "ingest_timestamp": random_timestamp_for_day(day)
            }
            es.index(index=INDEX, document=doc)
            total += 1

    print(f"✅ Generated and indexed {total} synthetic alerts over {DAYS} days from {len(OFFENDERS)} different IPs.")

if __name__ == "__main__":
    main()
