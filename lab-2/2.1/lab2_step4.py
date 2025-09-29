import re

with open('auth.log', 'r') as f:  # read file
    pattern = r"\d+\.\d+\.\d+\.\d+" # it's pattern for IPs
    ips = [] # empty list to store IPs
    for line in f: # looking for pattern in each line
        ips.append(re.findall(pattern, line)[0]) # findall looking for all matches for pattern, but we only take first, using [0] and add to list ips
    unique_ips = set(ips) # i use set to remove duplicates
    with open('unique_ips.txt', 'w') as y: # w - means write
        for ip in unique_ips: 
            y.write(ip + '\n') # writing each unique IP to new file
        
        #task 3.4

