import re

pattern = r"at"  # changed cat to at
text = "The cat sat on the mat."
#task 2.1
matches = re.findall(pattern, text)
print(matches) # Output: 'at', 'at', 'at'] beacause of cat, sat, mat