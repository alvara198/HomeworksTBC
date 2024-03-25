user_input = input("შეიყვანეთ ტექსტი: ")
user_input = user_input.lower()
allowed = "qwertyuiopasdfghjklzxcvbnm"
clean_user_input = ""
for c in user_input:
    if allowed.find(c) > -1:
        clean_user_input += c

mirror = ""

for i in range(len(clean_user_input)-1, -1, -1):
    mirror += clean_user_input[i]

if mirror == clean_user_input:
    print("Is palindrome")
else:
    print("is not palindrome")