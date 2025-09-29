import re

pattern = r"[A-Za-z]+" # r - raw string, #/d - number (0-9), /d+ - number, A-Za-z - all letters, A-Z - capital letters, a-z - small letters, + - one or more
text = "Order 123 was placed on 2023-05-01."
#task 2.2
print(re.findall(pattern, text))