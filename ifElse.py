import time

timeStamp = time.strftime("%H:%M:%S")
print(timeStamp)
hour = int(time.strftime("%H"))
print(hour)
min = int(time.strftime("%M"))
print(min)
sec = int(time.strftime("%S"))
print(sec)
if (hour < 12) or (hour >= 6):
    print("Good Morning")
elif (hour >= 12) or (hour <= 4):
    print("Good afternoon")
elif (hour >= 4) or (hour <= 7):
    print("Good Evening")
else:
    print("Good night")
