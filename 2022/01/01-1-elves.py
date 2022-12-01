# calculate which elve have the most calories
list = []
current_total_cals = 0
count = 0
while True:
    user_input = input()

    # 👇️ if user pressed Enter without a value, break out of loop
    if user_input == '':
        count += 1
        list.append(current_total_cals)
        current_total_cals = 0
        if user_input == '' and count == 2:
            count = 0
            break
    else:
        count = 0
        current_total_cals += int(user_input)

# 👇️ prints list of strings
#sum(sorted(list)[-3:])
print(sum(sorted(list)[-3:]))