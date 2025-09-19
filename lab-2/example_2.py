with open('sample.txt', 'r') as f:
    for i, line in enumerate(f, start=1): # i use enumerate to count lines, start=1 because usually python starts from 0
        print(f"{i}: {line.strip()}") # f give me ability to use variables inside string
#task 1.2