f = open(".\Day1\Star2\Input.txt", "r")
ary = f.read().split("\n\n")
high1 = 0
high2 = 0
high3 = 0
for elf in ary:
    cur = 0
    for cal in elf.split("\n"):
        cur += int(cal)
    if cur > high1:
        high3 = high2
        high2 = high1
        high1 = cur
    else:
        if cur > high2:
            high3 = high2
            high2 = cur
        else:
            if cur > high3:
                high3 = cur
print(high1 + high2 + high3)
