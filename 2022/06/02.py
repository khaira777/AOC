from collections import deque, Counter
def isUniqueChars(string):
    # Counting frequency
    freq = Counter(string)
    return len(freq) == len(string)

with open('input.txt') as f:
    lines = f.readlines()
    packet = deque()
    # print("before: ", packet)
    for i,val in enumerate(lines[0]):
        packet.append(val)
        if len(packet) < 14:
            # print("if: ", packet)
            continue
        else:
            # print("else: ", packet)
            if isUniqueChars(packet):
                # print(''.join(packet))
                print(i+1)
                break
            packet.popleft()