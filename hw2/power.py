def power(a,b):
#""" computes a**b using iterated squaring """
    result=1
    while b>0: # b is nonzero
        if b % 2 == 1: # b is odd
            result = result*a # )פעולת כפל אחת(
            print ("if")
        a = a*a # )פעולת כפל אחת(
        print ("a",a)
        b = b//2
        print("b",b)
        #print (result)
    return result
