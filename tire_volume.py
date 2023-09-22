import math

w = float(input("enter the width of the tire in mm:"))
print()
r = float(input("enter the aspect ratio of the tire:"))
print()
d = float(input("enter the diameter of the wheel in inches"))
print()
quest = input("Do you want to purchase this?")
print()
if quest == "yes".lower():
    ans = input("Please enter your contact number:")
if quest == "no".lower():
    print("Thank you for visiting, GOOD BYE!")
num1 = 2540
brackets = (w*r)
num = 10000000000
v = math.pi*w*w*r*(w*r+num1*d)/num

print(f"The approximate volume is {v:.2f} liters.")


from datetime import datetime
current_date_and_time = datetime.now()
print(current_date_and_time)

with open("volume.txt", "at") as volume_files:
 print(f"{current_date_and_time:%y-%m-%d},{w},{r},{d},{v:.2f},{ans}", file=volume_files)