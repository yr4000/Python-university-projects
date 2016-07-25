def find_root(f, a, b, EPS=0.001):
    if (f(a)>0 and f(b)>0) or (f(a)<0 and f(b)<0):
        print("YOU LIAR!!!!")
        return None
       
    # Keilus storage:
    neg = None; pos = None ; c = None; avrg = None
    
    if f(a)>0: pos = a; neg = b
    else: pos = b; neg = a

    if (f(a)**2) > (f(b)**2): avrg = f(b)
    else: avrg = f(a)
    
    while abs(avrg) > abs(EPS):
        c = (pos+neg)/2
        avrg = f(c)
        if avrg > 0: pos = c
        else: neg = c
        print ("c is: " , c)
        print ("neg: " , neg)
        print ("pos: " , pos)

    return c


        


    

        
        
    
    
