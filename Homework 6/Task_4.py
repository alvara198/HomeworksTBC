wveti = int(input("შემოიყვანეთ რიცხვი 1-დან 10-მდე: "))
xazi = ""
ricxvi = 1

while 1 > wveti or wveti >= 10:
    wveti = int(input("პროგრამა მიიღებს მხოლოდ რიცხვს 1-დან 10-მდე! შეიყვანეთ თავიდან: "))

"""
ამას ვიზამდი რომ "მცოდნოდა" substring ები.
მაგრამ შევეცდები არ გამოვიყენო და საქმე გავირთულო :) 

while ricxvi <= wveti:
    xazi += f"{ricxvi} "
    ricxvi += 1
    print(xazi)

while ricxvi > 2:
    xazi = xazi[0:(len(xazi)-2)]
    print(xazi)
    ricxvi -= 1
    
"""

xazisrigi = 1
while xazisrigi <= wveti-1:

    while ricxvi <= xazisrigi:
        print(ricxvi, end=" ")
        ricxvi += 1

    ricxvi = 1
    xazisrigi += 1
    print()

while xazisrigi > 0:

    while ricxvi <= xazisrigi:
        print(ricxvi, end=" ")
        ricxvi += 1

    ricxvi = 1
    xazisrigi -= 1
    print()
