import fileinput
points = 0
for line in fileinput.input(files ='values01.txt'):
    hm = {"X":1,"Y":2,"Z":3}
    #win
    if (line[0] == 'A' and line[2] == 'Y') or (line[0] == 'B' and line[2] == 'Z') or (line[0] == 'C' and line[2] == 'X'):
        points += 6
    #loss
    if (line[0] == 'A' and line[2] == 'Z') or (line[0] == 'B' and line[2] == 'X') or (line[0] == 'C' and line[2] == 'Y'):
        points += 0
    #draw
    if (line[0] == 'A' and line[2] == 'X') or (line[0] == 'B' and line[2] == 'Y') or (line[0] == 'C' and line[2] == 'Z'):
        points += 3
    points += hm[line[2]]
print(points)