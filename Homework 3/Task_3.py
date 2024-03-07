import random

color = random.randint(0, 4)
ricxvi = random.randint(2, 13)

randomcard = "Your random card is "

if ricxvi == 10:
    randomcard += "Jack"
elif ricxvi == 11:
    randomcard += "Queen"
elif ricxvi ==  12:
    randomcard += "King"
elif ricxvi == 13:
    randomcard += "Ace"
else:
    ricxvi = str(ricxvi)
    randomcard += ricxvi

if color == 0:
    randomcard += " of clubs"
elif color == 1:
    randomcard += " of diamonds"
elif color == 3:
    randomcard += " of spades"
else:
    randomcard += " of hearts"

print(randomcard)
