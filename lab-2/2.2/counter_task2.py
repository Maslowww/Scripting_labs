from collections import defaultdict

def ip_parse(line):
    # Простая примерная реализация - парсим IP из строки, предполагая формат "from IP"
    # Нужно переделать под конкретный формат лога
    import re
    match = re.search(r'(\d+\.\d+\.\d+\.\d+)', line)
    if match:
        return match.group(1)
    else:
        return None

counts = defaultdict(int)  # Счетчик для IP

with open("sample_auth_small.log") as f:
    for line in f:
        if "Failed password" in line or "Invalid user" in line:
            ip = ip_parse(line)
            if ip:
                counts[ip] += 1

print(counts)
