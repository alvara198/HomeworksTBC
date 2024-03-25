import random
import math
user_input = int(input("შეიყვანეთ რიცხვი: "))
while not user_input > 1:
    user_input = int(input("შეიყვანეთ 1-ზე დიდი ნატურალური რიცხვი: "))

count = 0

for i in range(user_input):
    a = random.random()
    while a == 0:
        a = random.random()

    b = random.random()
    while b == 0:
        b = random.random()

    if math.sqrt(a**2 + b**2) <= 1:
        count += 1

print(4*count/user_input)
