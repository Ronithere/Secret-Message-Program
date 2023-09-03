#creaeted by - ronit
#github username - Ronithere
import random 
from time import sleep
from typing import final 
l = 'abcdefghijklmnopqrstuvwxyz'
l2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBER="0123456789"
Symbol='[]{}*^()-_,>>'
all = l + l2 + NUMBER + Symbol
length=(3)
choice1 = "".join(random.sample(all,length))
choice2 = "".join(random.sample(all,length))
choice3 = "".join(random.sample(all,length))
choice4 = "".join(random.sample(all,length))
choice5 = "".join(random.sample(all,length))

print("Welcome To Secret Message Program By Ronit..")
sleep(1)
option = input('\nType 1 for Writing Message:  \nor\nType 2 for Solving the given message:\n Type your answer:  ')


if (option == "1"):
    data1 = str(input("Enter Your Message: "))
    print("Your Message Is Loading...")
    sleep(2)
    data2 = data1.split(" ")
    data = []
    for element in data2:
        if len(element) == 2:
            shuffle = element[::-1]
            word = choice3 + shuffle + choice2
            data.append(word)

        elif len(element) > 2:
            code0 = choice1 + element[1:] + element[0] + choice5
            data.append(code0)

        elif len(element) == 1:
            shuffle = element[::-1]
            word = choice5 + shuffle + choice1
            data.append(word)
    print('''\nYour Secret Message Is: ''',(" ".join(data)))

elif option == '2':
    data4 = str(input("Enter Your Given Secret Message: "))
    print("Your Message Is Solving...")
    sleep(2)
    data3 = data4.split(" ")
    data5 = []
    for element1 in data3:
        if len(element1) == 2:
            message0 = element1[3:-3]
            msg = message0[-1]+message0[:-1]
            data5.append(msg)
        else:
          print("Enter a valid secret message")
            # message0 = element1[3:-3]
            # msg = message0[-1]+message0[:-1]
            # data5.append(msg) 
    print('\nYour Secret Solved Message Is: ',(" ".join(data5))) 
