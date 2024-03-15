n = input("შეიყვანეთ რიცხვი 0-დან 10000-მდე: ")

while not 0 <= int(n) < 10000:
    n = input("რიცხვი გაცდა ზღვარს! შეიყვანეთ თავიდან: ")

length = len(n)
counter = 0
sum = 0
reversed = ""

while counter < length:

    reversed += n[length - 1 - counter]
    sum += int(n[length - 1 - counter])
    counter += 1

print(f"reversed = {reversed}\nsum = {sum}")