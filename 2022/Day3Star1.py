f = open(".\Day3\Star1\Input.txt", "r")
ary = f.read().split("\n")
count = 0
for line in ary:
    first, second = line[:len(line)//2], line[len(line)//2:]
    c = ''.join(set(first).intersection(second))
    if c.isupper():
        count += (ord(c) - 64 + 26)
    else:
        count += (ord(c) - 96)
print(count)
