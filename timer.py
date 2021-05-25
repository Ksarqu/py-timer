from time import sleep
from os import system

LeftTime = int(input("Enter Time in seconds: "))
while LeftTime > 0:
    print(f"Time to end: {LeftTime}")
    LeftTime -= 1
    sleep(1)
    system("cls")
    
print("Time has elapsed")

#dsggnklsedhduioghuosjebhojik'sdrnjikop