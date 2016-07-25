k = int(input("Welcome to K-Boom! Please insert a Boom (an integer between 1-9 ONLY!)"))
if k>9 or k == 0:
    print ("You have just broke the rules! You lost!")
    quit()
n = int(input("Great! Now please enter any integer: "))
print ("Let the game begin!")
for num in range(1,n+1):
    snum = str(num)
    k_in = None
    k_mod = None
    for dig in snum:
        if dig == str(k): k_in = True
        else: k_in = False
    if num%k == 0 : k_mod = True
    else: k_mod = False

    if k_in is True and k_mod is True: print ("Boom-Boom!")
    elif k_in is False and k_mod is True: print ("Boom!")
    else: print (num)
    
print ("Yay! wasn't that FUN?!")
print ("BYE!")
