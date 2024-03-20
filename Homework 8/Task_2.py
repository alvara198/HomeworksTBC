user_input = input("შეიყვანეთ ტექსტი: ")
valid_symbols = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"
for c in user_input:
    if valid_symbols.find(c) != -1:
        print(c, end="")
print()
