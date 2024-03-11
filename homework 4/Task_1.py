import random

Players = int(input('შეიყვანეთ მოთამაშეთა რაოდენობა: '))

if Players < 1:
    print("შეიყვანეთ მოთამაშეთა რაოდენობა, რომელიც აღემატება 1-ს!")
else:
    for i in range(1, Players+1):
        Dice1 = random.randint(1, 6)
        Dice2 = random.randint(1, 6)
        print(f'მოთამაშე #{i} გააგორა: {Dice1}, {Dice2}.')
