import random
Frukter =("apelsin","äpple", "banan")
looping = True


while looping:
    i =1
    for frukt in Frukter:
        print(str(i) + frukt)
        i  = i+1
    
    
    
    
    go = input("vill du välja en frukt till? j/n ")
    print("\n")

    if (go == "n"):
        break


