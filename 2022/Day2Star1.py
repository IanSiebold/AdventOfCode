f = open("Input.txt", "r")
ary = f.read().split("\n")
score = 0
for game in ary:
    if game[0] == 'A':
        if game[2] == 'X':
            score += 3 #Rock Rock Tie
            score += 1 #Rock
        if game[2] == 'Y':
            score += 6 #Rock Paper Win
            score += 2 #Paper
        if game[2] == 'Z':
            score += 0 #Rock Scissors Loss
            score += 3 #Scissors
    if game[0] == 'B':
        if game[2] == 'X':
            score += 0 #Paper Rock Loss
            score += 1 #Rock
        if game[2] == 'Y':
            score += 3 #Paper Paper Tie
            score += 2 #Paper
        if game[2] == 'Z':
            score += 6 #Paper Scissors Win
            score += 3 #Scissors
    if game[0] == 'C':
        if game[2] == 'X':
            score += 6 #Scissors Rock Win
            score += 1 #Rock
        if game[2] == 'Y':
            score += 0 #Scissors Paper Loss
            score += 2 #Paper
        if game[2] == 'Z':
            score += 3 #Scissors Scissors Tie
            score += 3 #Scissors
print(score)
