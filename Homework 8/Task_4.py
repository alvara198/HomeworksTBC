line_encrypt = "qwertyuiopqasdfghjklazxcvbnmz"
line_decrypt = "zmnbvcxzalkjhgfdsaqpoiuytrewq"
user_action = input("encrypt or decrypt(e/d): ")
user_text = input("enter the text: ")
while user_action != "e" and user_action !="d":
    user_action = input("incorrect ation enter again(e/d): ")
result = ""

if user_action == "e":
    for c in user_text:
        c_index = line_encrypt.find(c)
        if c_index>-1:
            result += line_encrypt[c_index+1]
        else:
            result += c
else:
    for c in user_text:
        c_index = line_decrypt.find(c)
        if c_index>-1:
            result += line_decrypt[c_index+1]
        else:
            result += c

print(result)
