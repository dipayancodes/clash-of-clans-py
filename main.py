import time
import random
input("Select your troops down bellow, press ENTER ")

binfo = open("info.txt", 'r')

print(binfo.readline())
b = int(input("how many barberians you wanna train: "))
print(binfo.readline())
a = int(input("how many archer you wanna train: "))
print(binfo.readline())
w = int(input("how many wizard you wanna train: "))
print(binfo.readline())
g = int(input("how many giant you wanna train: "))

totaltroops = b + a + w + g

print("FINDING A BATTLE FOR YOU ....")
time.sleep(3)
print("BATTLE FOUND !")
time.sleep(2)
print("battleing with your opponent...")
time.sleep(10)

stars = random.randrange(1,3)
accuracy = random.randrange(1,99)

if stars >= 1:
    print(f"You won , and got {stars} with the accuracy of {accuracy}% ")
else:
    print("you lost better luck next time")
