k = 3
n = 100
for num in range(1,n+1):
    snum = str(num)
    k_in = None
    k_mod = None
    for dig in snum:
        if dig == str(k): k_in = True
        if num%k == 0 : k_mod = True
        else: k_mod = False

    if k_in is True and k_mod is True: print ("boom-boom!")
    elif k_in is True or k_mod is True: print ("boom!")
    else: print (num)
    
