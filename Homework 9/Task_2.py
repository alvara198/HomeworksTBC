FIRST_STR = input("Enter first text: ")
first_str = FIRST_STR
SECOND_STR = input("Enter second text: ")
second_str = SECOND_STR

for c in FIRST_STR:
    index = int(second_str.find(c))
    if index > -1:
        second_str = second_str[0:index] + second_str[index+1:len(second_str)]
    else:
        print("Output: NO")
        exit()

second_str = SECOND_STR

for c in SECOND_STR:
    index = int(first_str.find(c))
    if index > -1:
        first_str = first_str[0:index] + first_str[index+1:len(first_str)]
    else:
        print("Output: NO")
        exit()

print("Output: YES")
