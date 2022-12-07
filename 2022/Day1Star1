f = open("Input.txt", "r")
ary = f.read().split("\n\n")
high = 0
for elf in ary:
    cur = 0
    for cal in elf.split("\n"):
        cur += int(cal)
    if cur > high:
        high = cur
print(high)
