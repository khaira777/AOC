with open('input.txt') as f:
    # list to store all stacks
    all_stacks = []
    
    lines = f.readlines()
    
    # total stacks
    stacks_total = len(lines[0])//4
    
    # initialize empty lists (stacks)
    for i in range(stacks_total):
        all_stacks.append(list())
    
    stack_bottom = 0
    operation_start = 0
    for i,line in enumerate(lines):
        # print(i)
        
        # check at what index the moving starts
        if line.strip() == "":
            # print(f'start appending items into stacks from 0 until {i-2}')
            stack_bottom = i-2
            # print(f'do operations from {i+1}')
            operation_start = i+1
            break

    # add crates to stacks # preprocessing
    done_until = stack_bottom
    while done_until+1 > 0:
        # print("doing:", lines[done_until])
        for i, value in enumerate(lines[done_until]):
            # print(i, value)
            if (i+3)%4 == 0 and value.strip() != "":
                all_stacks[((i+3)//4)-1].append(value)
                # print(f"add value: {value} in stack: {(i+3)//4}")
        done_until -= 1
    # print(all_stacks)
    
    # operation start here
    # print("operation_start", operation_start)
    total_movings = 0
    from_stack = 0
    to_stack = 0
    the_operation = []
    total_operation = len(lines)
    for i in range(operation_start, total_operation):
        # print(lines[i])
        the_operation = lines[i].split(" ")
        total_movings, from_stack, to_stack = int(the_operation[1].strip()), int(the_operation[3].strip()), int(the_operation[5].strip())
        # print(total_movings, from_stack, to_stack)
        for i in range(total_movings):
            all_stacks[to_stack-1].append(all_stacks[from_stack-1].pop())
    # print(all_stacks)
    for i in all_stacks:
        print(i.pop())