import fileinput
count = 0
for line in fileinput.input(files ='input.txt'):
    pair_work = line.split(",")
    elf1 = list(range(int(pair_work[0].split("-")[0]),int(pair_work[0].split("-")[1])+1))
    elf2 = list(range(int(pair_work[1].split("-")[0]),int(pair_work[1].split("-")[1])+1))
    if set(elf1).issubset(set(elf2)) or set(elf2).issubset(set(elf1)):
        count += 1
print(count)