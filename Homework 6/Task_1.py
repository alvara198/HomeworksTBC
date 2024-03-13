i = 1
j = 2
while i < 9:

    xazi = f"1*{i}={i}"

    while j <= i:

        if (i == 3 and j == 3) or (i == 4 and j == 3):  #ეს if statement სვეტებს ასწორებ
            xazi += " "

        xazi += f" {j}*{i}={j*i}"
        j += 1

    i += 1
    j = 2

    print(xazi)
