user_input = input("შეიყვანეთ ტექსტი: ")

first_char = user_input[0]
last_char = user_input[-1]
if len(user_input) % 2 == 0:
    middle_char = user_input[len(user_input)//2-1] + user_input[len(user_input)//2]
else:
    middle_char = user_input[len(user_input)//2]

count = 0
while count < 15:
    if count < 5:
        print(last_char, end="")
    elif count < 10:
        print(first_char, end="")
    else:
        print(middle_char, end="")

    count += 1
