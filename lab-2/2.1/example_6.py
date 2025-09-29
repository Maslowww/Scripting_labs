import re

pattern = r"\d+\.\d+\.\d+\.\d+" # it's patter for ip, it's too mant d+ and . - becasuse ip have 4 parts of numbers separated by dots
text = "Failed login from 192.168.0.1 and 10.0.0.5 at 10:30" #add new ip for task
#task 2.3
print(re.findall(pattern, text))