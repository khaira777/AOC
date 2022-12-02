import fileinput
points = 0
for line in fileinput.input(files ='values01.txt'):
    hm = {"X":1,"Y":2,"Z":3}
    #lose
    if (line[2]=="X"):
        lose_hm={"A":"Z","B":"X","C":"Y"}
        points += 0 # for loss
        choice = lose_hm[line[0]]
        points += hm[choice] # for choice
    #draw
    if (line[2]=="Y"):
        draw_hm={"A":"X","B":"Y","C":"Z"}
        points += 3 # for draw
        choice = draw_hm[line[0]]
        points += hm[choice] # for choice
    #win
    if (line[2]=="Z"):
        win_hm={"A":"Y","B":"Z","C":"X"}
        points += 6 # for win
        choice = win_hm[line[0]]
        points += hm[choice] # for choice
print(points)