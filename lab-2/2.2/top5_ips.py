from collections import defaultdict
import time

def ip_parse(line):
    if " from " in line:
        parts = line.split()
        try:
            anchor = parts.index("from")
            return parts[anchor + 1].strip()
        except (ValueError, IndexError):
            return None
    return None

def top_n(counts, n=5):
    return sorted(counts.items(), key=lambda kv: kv[1], reverse=True)[:n]

counts = defaultdict(int)

start = time.time()

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

end = time.time()

top_5 = top_n(counts, 5)

print("Top 5 attacker IPs:")
for rank, (ip, count) in enumerate(top_5, start=1):
    print(f"{rank}. {ip} — {count}")

with open('failed_counts.txt', 'w') as out_file:
    out_file.write("ip,failed_count\n")
    for ip, count in counts.items():
        out_file.write(f"{ip},{count}\n")

print("Wrote failed_counts.txt")
print("Elapsed:", round(end-start, 2), "seconds")
