password = "admin"

input_password = input("პაროლი(3 ცდა გაქვთ): ")

for i in range(2):
    if input_password != password:
        input_password = input("არასწორი პაროლია! შეიყვანეთ თავიდან:")

if input_password == password:
    print(" :) ")
else:
    print("blocked")
