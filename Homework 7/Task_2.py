n = int(input("შეიყვანეთ რიცხვი 1-დან 1001-მდე: "))

while not 0 < n <= 1000:
    n = int(input("რიცხვი გაცდა ზღვარს! შეიყვანეთ თავიდან: "))

while n != 1:
    n = int(n)
    print(f"{n} -> ", end = "")
    if n % 2 == 0:
        n /= 2
    else:
        n = 3*n + 1

print("1")