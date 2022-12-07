f = open(".\Day4\Star1\Input.txt", "r")
ary = f.read().split("\n")
count = 0
for line in ary:
    elf = line.split(',')
    elf1 = elf[0].split('-')
    elf2 = elf[1].split('-')
    if int(elf1[0]) <= int(elf2[0]) and int(elf1[1]) >= int(elf2[1]):
        count += 1
    elif int(elf2[0]) <= int(elf1[0]) and int(elf2[1]) >= int(elf1[1]):
        count += 1
print(count)
