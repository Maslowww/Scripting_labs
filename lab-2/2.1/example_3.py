with open('sample.txt', 'r') as f: #r - means read
    with open('copy.txt', 'w') as y: # w - means write
        for line in f: #iterating each line of the file
            y.write(line) # writing each line to new file

#task 1.3

    # f.write("This is a new file.\n")       - code from example_3.py
    # f.write("It has two lines.\n")         - code from example_3.py