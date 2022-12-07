f = open(".\Day5\Star1\Input.txt", "r")
ary = f.read().split("\n")
stacks = [[],[],[],[],[],[],[],[],[]]
#First initialize with the 8 by 9 grid at the top starting from the bottom of the stack WARNING THIS IS VERY UGLY
for i in reversed(range(8)):
    line = ary[i]
    if line[1] != ' ':
        stacks[0].append(line[1])
    if line[5] != ' ':
        stacks[1].append(line[5])
    if line[9] != ' ':
        stacks[2].append(line[9])
    if line[13] != ' ':
        stacks[3].append(line[13])
    if line[17] != ' ':
        stacks[4].append(line[17])
    if line[21] != ' ':
        stacks[5].append(line[21])
    if line[25] != ' ':
        stacks[6].append(line[25])
    if line[29] != ' ':
        stacks[7].append(line[29])
    if line[33] != ' ':
        stacks[8].append(line[33])
#Now logic to follow the rules but first remove top 10 lines to get rid of init setup
del ary[:10]
for rule in ary:
    words = rule.split(' ')
    move = int(words[1])
    #0 index so subtract 1 to match up with index
    start = int(words[3]) - 1
    dest = int(words[5]) - 1
    while move > 0:
        stacks[dest].append(stacks[start].pop())
        move -= 1
print(stacks)
