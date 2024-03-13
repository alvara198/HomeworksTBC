simagle = int(input("გთხოვთ, შეიყვანეთ რიცხვი 1-დან 10-მდე: "))
xazisrigi = 0

while 9 < simagle or 1 > simagle:
    simagle = int(input("პროგრამა მიიღებს მხოლოდ რიცხვს 1-დან 10-მდე! შეიყვანეთ თავიდან: "))

while xazisrigi <= simagle:
    marcxena = ""
    marjvena = ""
    ricxvi = xazisrigi

    marcxena += (" " * 2 * (simagle - xazisrigi))
    while ricxvi >= 1:
        marcxena += f"{ricxvi} "
        ricxvi -= 1
    marcxena += "0"
    print(marcxena, end="")

    while ricxvi < xazisrigi:
        ricxvi += 1
        marjvena += f" {ricxvi}"

    print(marjvena)
    xazisrigi += 1
