Shekvanili = int(input("შეიყვანეთ რიცხვი 1-დან 50-მდე: "))

if 0 < Shekvanili < 50:
    for i in range(1, Shekvanili+1):

        xazi = f"{i} -"
        count = 0

        for j in range(1, i+1):

            if i % j == 0:
                xazi += f" {j}"

                count += 1

            if count == 3:
                break

        print(xazi)
else:
    print("თქვენ მიერ შეყვანილი რიცხვი გასცდა ზღვარს!")
