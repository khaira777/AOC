import fileinput
count = 0
for line in fileinput.input(files ='input.txt'):
    pair_work = line.split(",")
    elf1 = tuple(range(int(pair_work[0].split("-")[0]),int(pair_work[0].split("-")[1])+1))
    elf2 = tuple(range(int(pair_work[1].split("-")[0]),int(pair_work[1].split("-")[1])+1))
    if any(item in elf1 for item in elf2):
        count += 1
print(count)