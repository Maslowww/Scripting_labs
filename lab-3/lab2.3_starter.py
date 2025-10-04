import re
import json
from datetime import datetime, timedelta
import matplotlib.pyplot as plt  # <-- for plotting, must be installed

ip_attempts = {}
log_file = "sample_auth_small.log"
year = "2025"
date_format = "%Y %b %d %H:%M:%S"
pattern = r"(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}).*Failed password.*from\s+(\d+\.\d+\.\d+\.\d+)"

with open(log_file, "r") as f:
    for line in f:
        match = re.search(pattern, line)
        if match:
            ts_str = match.group(1)
            ip = match.group(2)
            full_date_str = f"{year} {ts_str}"
            try:
                dt = datetime.strptime(full_date_str, date_format)
                ip_attempts.setdefault(ip, []).append(dt)
            except ValueError:
                print(f"Error parsing date: {full_date_str}, line: {line.strip()}")

for ip in ip_attempts:
    ip_attempts[ip].sort()

incidents = []
window = timedelta(minutes=10)
for ip, times in ip_attempts.items():
    n = len(times)
    i = 0
    while i < n:
        j = i
        while j + 1 < n and (times[j + 1] - times[i]) <= window:
            j += 1
        count = j - i + 1
        if count >= 5:
            incidents.append({
                "ip": ip,
                "count": count,
                "first": times[i].isoformat(),
                "last": times[j].isoformat()
            })
            i = j + 1
        else:
            i += 1

print(f"Detected {len(incidents)} brute-force incidents")
for incident in incidents[:5]:
    print(incident)

with open("bruteforce_incidents.txt", "w") as f:
    json.dump(incidents, f, indent=2)

# -- Diagram section: Top IPs by failed attempts --
ip_counts = {ip: len(times) for ip, times in ip_attempts.items()}
top_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]
ips = [ip for ip, _ in top_ips]
counts = [count for _, count in top_ips]

plt.figure(figsize=(10, 6))
plt.bar(ips, counts, color='red')
plt.title("Top Attacker IPs")
plt.xlabel("IP Address")
plt.ylabel("Failed Attempts")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_attackers.png")
plt.show()

