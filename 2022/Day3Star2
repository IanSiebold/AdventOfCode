f = open(".\Day3\Star2\Input.txt", "r")
ary = f.read().split("\n")
count = 0
i = 0
while i < len(ary) - 2:
    first, second, third = ary[i], ary[i + 1], ary[i + 2]
    i += 3
    c = ''.join(set(first).intersection(second))
    c = ''.join(set(c).intersection(third))
    if c.isupper():
        count += (ord(c) - 64 + 26)
    else:
        count += (ord(c) - 96)
print(count)
