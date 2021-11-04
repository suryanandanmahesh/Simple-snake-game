import time
from playsound import playsound

playsound('Smart_Assistant/Sound/f.mp3')
a = input("First number: ")
a = float(a)
playsound('Smart_Assistant/Sound/o.mp3')
o = input("Operation( + or - or / or x ):")
playsound('Smart_Assistant/Sound/s.mp3')
b = input("Second number: ")
b = float(b)    
t = 3

if o == "+":
    q = float(a+b)
    print("")
    print("Ok! ",a,"+",b,"=",q)
    playsound('Smart_Assistant/Sound/7.mp3')
    print("")
    time.sleep(t)

elif o == "-":
    w = float(a-b)
    print("")
    print("Ok! ",a,"-",b,"=",w)
    playsound('Smart_Assistant/Sound/7.mp3')
    print("")
    time.sleep(t)

elif o == "/":
    z = float(a-b)
    print("")
    print("Ok! ",a,"/",b,"=",z)
    playsound('Smart_Assistant/Sound/7.mp3')
    print("")
    time.sleep(t)

elif o == "x":
    t = float(a*b)
    print("")
    print("Ok! ",a,"x",b,"=",t)
    playsound('Smart_Assistant/Sound/7.mp3')
    print("")
    time.sleep(t)

elif o == "*":
    t = float(a*b)
    print("")
    print("Ok! ",a,"x",b,"=",t)
    playsound('Smart_Assistant/Sound/7.mp3')
    print("")
    time.sleep(t)
else:
    print("Invalid operation")

import main