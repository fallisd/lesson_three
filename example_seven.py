subjects = ['physics', 'chemistry', 'biology', 'math', 'english']

count = 1

for subject in subjects:

    label = "Subject " + count + ": " + subject
    print(label) # What we expect: Subject 1: physics 
    count = count + 1