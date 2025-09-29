with open('sample_auth_small.log', 'r') as f:

    def ip_parse(line):
        if " from " in line:
            parts = line.split()
            try:
                anchor = parts.index("from")
                return parts[anchor + 1].strip()
            except (ValueError, IndexError):
                return None
        return None

    unique_ips = set()
    total_lines = 0

    for line in f:
        total_lines += 1
        ip = ip_parse(line)
        if ip:
            unique_ips.add(ip)

print("Total lines read:", total_lines)
print("Number of unique IPs:", len(unique_ips))
print("First 10 unique IPs (sorted):", sorted(unique_ips)[:10])
