
ricxvi = int(input("შეიყვანეთ 11-ზე ნაკლები ნატურალური რიცხვი: "))

if ricxvi > 10 or ricxvi < 0:
    print("თქვენს მიერ შეყვანილი რიცხვი არ აკმაყოფილებს პირობას!")
else:
    pasuxi = "მოცემული რიცხვის მარტივი გამყოფებია:"

    if ricxvi % 2 == 0:
        pasuxi += " 2,"

    if ricxvi % 3 == 0:
        pasuxi += " 3,"

    if ricxvi % 5 == 0:
        pasuxi += " 5,"

    if ricxvi % 7 == 0:
        pasuxi += " 7,"

    if pasuxi == "მოცემული რიცხვის მარტივი გამყოფებია:":
        print("მოცემულ რიცხვს არ აქვს მარტივი გამყოფი.")
    else:
        pasuxi = pasuxi[0:len(pasuxi) - 1]
        pasuxi += '.'
        print(pasuxi)
