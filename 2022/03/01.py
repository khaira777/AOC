import fileinput
priority = 0
for line in fileinput.input(files ='values01.txt'):
    comp1 = line[:len(line)//2]
    comp2 = line[len(line)//2:]
    for i in comp1:
        if i in comp2:
            if i.islower():
                priority += ord(i)-96
                break
            else:
                priority += (ord(i)-64)+26
                break
print(priority)