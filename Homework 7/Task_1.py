n = int(input("შეიყვანეთ რიცხვი 0-დან 20-მდე: "))

while not 0 <= n < 20:
    n = int(input("რიცხვი გაცდა ზღვარს! შეიყვანეთ თავიდან: "))

previous = 0
next = 1
counter = 0

while counter < n:
    print(previous, end=" ")
    previous += next
    next, previous = previous, next
    counter += 1
