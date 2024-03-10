height = int(input("შეიყვანეთ ნაძვის ხის სიმაღლე(1-დან 50-მდე): "))

if 0 < height < 50:

    print(" "*(height) + "*")

    for i in range(1, height):
        xazi = " "*(height-i) + "/"*(i) + "|" + "\\"*(i)
        print(xazi)

    print(" " * (height) + "|")

else:
    print("თქვენ მიერ შეყვანილი რიცხვი ცდება ზღვარს!")
