import random

chafiqrebuli = random.randint(0, 99)
count = 2

cda = int(input("კომპიუტერმა ჩაიფიქრა რიცხვი! შეეცადე გამოიცნო (სულ გექნება 10 ცდა): "))

while cda != chafiqrebuli:

    if cda > chafiqrebuli:
        cda = int(input(f"კომპიუტერის ჩაფიქრებული რიცხვი ნაკლებია. ცდა #{count}: "))
    else:
        cda = int(input(f"კომპიუტერის ჩაფიქრებული რიცხვი მეტია. ცდა #{count}: "))

    count += 1
    if count == 11:
        print("კომპიუტერმა დაგამარცხა! :(")
        break

if count < 11:
    print("You are a winner!")
