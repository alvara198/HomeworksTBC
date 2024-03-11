import random

Ricxvi = int(input("შეიყვანეთ ნატურალური რიცხვი 1-დან 30-მდე: "))

if 0 < Ricxvi < 30:
    udidesi = 0

    for i in range(Ricxvi):

        randomNumber = random.randint(0, 1000)

        if randomNumber > udidesi:
            udidesi = randomNumber

        print(randomNumber, end=" ")

    print(f"\nმათ შორის უდიდესი არის: {max}")
else:
    print("თქვენ მიერ შეყვანილი რიცხვი ცდება ზღვარს(1-დან, 30-მდე)! :)")
