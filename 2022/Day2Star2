f = open("Input.txt", "r")
ary = f.read().split("\n")
score = 0
for game in ary:
    if game[0] == 'A': #Elf Rock
        if game[2] == 'X': #Lose
            score += 0 
            score += 3 #Scissors
        if game[2] == 'Y': #Tie
            score += 3 
            score += 1 #Rock
        if game[2] == 'Z': #Win
            score += 6 
            score += 2 #Paper
    if game[0] == 'B': #Elf Paper
        if game[2] == 'X': #Lose
            score += 0 
            score += 1 #Rock
        if game[2] == 'Y': #Tie
            score += 3 
            score += 2 #Paper
        if game[2] == 'Z': #Win
            score += 6 
            score += 3 #Scissors
    if game[0] == 'C': #Elf Scissors
        if game[2] == 'X': #Lose
            score += 0 
            score += 2 #Paper
        if game[2] == 'Y': #Tie
            score += 3 
            score += 3 #Scissors
        if game[2] == 'Z': #Win
            score += 6 
            score += 1 #Rock
print(score)
