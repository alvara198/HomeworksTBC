user_input = input("შეიყვანეთ ტექსტი: ")
for i in range(0 , len(user_input), 2):
    if user_input[i] != "e":
        print(user_input[i], end="")
print()
