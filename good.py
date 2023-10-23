import random
import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

kot = (27, 23)
ote, laje = kot
x = random.randint(1, ote - 2)
y = random.randint(1, laje - 2)
pyej = '@'

person = [random.randint(1, ote - 2), 1]
mouvman_moun = [0, 1] 
kolonn = random.randint(1, ote - 2)

while True:
    clear_console()

    x_moun, y_moun = person

    for i in range(laje):
        for j in range(ote):
            if i == 0 or i == laje - 1:
                print("*", end=" ")
            elif j == 0 or j == ote - 1:
                print("*", end=" ")
            elif i == y and j == x:
                print(pyej, end=" ")
            elif i == y_moun and j == x_moun:
                print("M", end=" ")
            else:
                print(" ", end=" ")
        print()

    y_moun += mouvman_moun[1]
    if y_moun <= 0:
        y_moun = laje - 2 
        x_moun = random.randrange(1, ote - 2)  
    elif y_moun >= laje - 1:
        y_moun = 1 
        x_moun = random.randrange(1, ote - 2) 

    person[0], person[1] = x_moun, y_moun

    if x_moun == x and y_moun == y:
        print("Ou rankontre moun nan! Ou pedi jwèt la.")
        break

    time.sleep(0.33)

print("Jwèt la fini.")
Print("ChatGPT e kek mote de recherche edem, nou poko gen nivo pwogramasyon sa")
