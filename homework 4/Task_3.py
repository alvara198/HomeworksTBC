import sys

Ricxvi = int(input("შეიყვანეთ მთელი დადებითი რიცხვი, რომელიც მეტია 0-ზე და ნაკლებია 1000-ზე: "))

if Ricxvi > 999 or Ricxvi < 1:
    print("თქვენ მიერ შეყვანილი რიცხვი ცდება ზღვარს(1-დან, 1000-მდე)! :)")
    sys.exit()

text = 'ამ რიცხვის გამყოფები არის: '

for i in range(1, Ricxvi+1):
    if Ricxvi % i == 0:
        text += f" {i},"

text = text[0:len(text) - 1]
text += "."
print(text)
