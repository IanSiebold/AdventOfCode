f = open(".\Day6\Star1\Input.txt", "r")
line = f.read()
i = 4
e = 0
while e == 0:
    check = line[i-4:i]
    if len(set(check)) == len(check):
        e = 1
    i += 1
print(i - 1)
