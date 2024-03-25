year = int(input("Enter year: "))

day = int(input("Enter day: "))
while not 0 < day < 32:
    day = int(input("Enter proper day: "))

month = int(input("Enter month: "))
while not 0 < month < 13:
    month = int(input("Enter proper month: "))
if month < 10:
    month = f"0{month}"

hour = int(input("Enter hour: "))
while not -1 < hour < 25:
    hour = int(input("Enter proper hour: "))
if hour < 10:
    hour = f"0{hour}"

minute = int(input("Enter minute: "))
while not -1 < minute < 61:
    minute = int(input("Enter proper minute: "))
if minute < 10:
    minute = f"0{minute}"

second = int(input("Enter second: "))
while not -1 < second < 61:
    second = int(input("Enter proper second: "))
if second < 10:
    second = f"0{second}"

ms = int(input("Enter ms: "))
if ms < 0:
    ms = int(input("Enter proper ms: "))

timezone = int(input("Enter timezone: "))
while not -13 < timezone < 13:
    timezone = int(input("Enter proper timezeone: "))


if timezone > -1:
    if abs(timezone) < 10:
        timezone = f"0{abs(timezone)}"
        print(f"input:{year}-{month}-{day}T{hour}:{minute}:{second}.{ms}+{timezone}:00\nOutput: {day}-{month}-{year} {hour%12}:{minute}:{second} +{timezone[1]}")
        exit()
    else:
        print(f"input:{year}-{month}-{day}T{hour}:{minute}:{second}.{ms}+{timezone}:00\nOutput: {day}-{month}-{year} {hour%12}:{minute}:{second} +{timezone}")
        exit()

if timezone < 0:
    if abs(timezone) < 10:
        timezone = f"0{abs(timezone)}"
        print(f"input:{year}-{month}-{day}T{hour}:{minute}:{second}.{ms}-{timezone}:00\nOutput: {day}-{month}-{year} {hour%12}:{minute}:{second} -{timezone[1]}")
        exit()
    else:
        print(f"input:{year}-{month}-{day}T{hour}:{minute}:{second}.{ms}+{timezone}:00\nOutput: {day}-{month}-{year} {hour%12}:{minute}:{second} -{timezone}")
        exit()