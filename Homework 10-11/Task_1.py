#უუულამაზესი ამოცანაა, მადლობა
user_input = int(input("შეიყვანეთ რიცხვი: "))
while not user_input>1:
    user_input = int(input("შეიყვანეთ 1-ზე დიდი ნატურალური რიცხვი: "))

x = 0
k = 0

while k <= 2*(user_input-1):
    x += (-1)**k / (1 + 2 * k)
    k += 1

print(4*x)
