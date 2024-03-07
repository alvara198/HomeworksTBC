import sys
import datetime
from datetime import date

Year = int(input("შეიყვანეთ სასურველი წელი: "))
if Year > datetime.MAXYEAR or Year < datetime.MINYEAR:
    print("შეიყვანეთ წელი, რომელიც არის 1-დან 9999-მდე!")
    sys.exit()

Month = int(input("შეიყვანეთ სასურველი თვე რიცხვობრივ ფორმატში: "))
if Month > 12 or Month < 0:
    print("შეიყვანეთ თვის აღმნიშვნელი რიცხვი 1-დან 12-მდე!")
    sys.exit()

Day = int(input("შეიყვანეთ დღე: "))
if Day > 31 or Day < 1:
    print("შეიყვანეთ თვის სწორი დღე!")
    sys.exit()


DayOfTheWeek = date(Year, Day, Month).weekday()

if DayOfTheWeek == 0:
    print("შეყვანილი თარიღი იყო ორშაბათი")
elif DayOfTheWeek == 1:
    print("შეყვანილი თარიღი იყო სამშაბათი")
elif DayOfTheWeek == 2:
    print("შეყვანილი თარიღი იყო ოთშაბათი")
elif DayOfTheWeek == 3:
    print("შეყვანილი თარიღი იყო ხუთშაბათი")
elif DayOfTheWeek == 4:
    print("შეყვანილი თარიღი იყო პარასკევი")
elif DayOfTheWeek == 5:
    print("შეყვანილი თარიღი იყო შაბათი")
else:
    print("შეყვანილი თარიღი იყო კვირა")
