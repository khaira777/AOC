import fileinput
priority = 0
counter = 0
lines = []
for line in fileinput.input(files ='values01.txt'):
    if counter<3:
        lines.append(line)
    counter += 1
    if counter == 3:
        counter = 0
        for i in lines[0]:
            if i in lines[1] and i in lines[2]:
                if i.islower():
                    priority += ord(i)-96
                    break
                else:
                    priority += (ord(i)-64)+26
                    break
        lines = []
    
print(priority)