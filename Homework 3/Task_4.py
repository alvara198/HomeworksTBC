import forex-python
from forex_python.bitcoin import BtcConverter
from datetime import datetime
import sys
import datetime


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

if Year < 2013 and Month < 10 and Day < 1:
    print("შეიყვანეთ თარიღი არაუგვიანეს 2013 წლის 1 ოქტომბრისა!")
    sys.exit()


Investment = float(input("შეიყვანეთ ინვესტირებული თანხის რაოდენობა დოლარებში: "))



PriceNow = BtcConverter()
PriceNow.get_latest_price('USD')

