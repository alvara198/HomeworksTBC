Number = int(input("შეიყვანეთ 20-ზე ნაკლები არაუარყოფითი მთელი რიცხვი: "))

if -1 < Number < 20:
    pirveli = 0
    meore = 1

    for i in range(Number):
        pirveli += meore
        pirveli, meore = meore, pirveli

    print(pirveli)
else:
    print("თქვენ მიერ შეყვანილი რიცხვი ცდება ზღვარს [0, 20)!")
