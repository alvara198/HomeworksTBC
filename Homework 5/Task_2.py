
for i in range(1, 10):
    xazi = f"1*{i}={i}"
    for j in range(2, i+1):

        if (i == 3 and j == 3)  or (i == 4 and j == 3):  #ეს if statement სვეტებს ასწორებ
            xazi += " "

        xazi += f" {j}*{i}={j*i}"

    print(xazi)
