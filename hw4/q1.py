import time
def elapsed(expression,number=1):
    ''' computes elapsed time for executing code number of
    times (default is 1 time). expression should be a string
    representing a Python expression. '''
    t1=time.clock()
    for i in range(number):
        eval(expression)
        t2=time.clock()
        return t2-t1

def max1(L):
    if len(L)==1:
        return L[0]
    return max(L[0], max1(L[1:])) #complexity O(n**2)?


def max2(L):
    if len(L)==1:
        return L[0]
    l = max2(L[:len(L)//2])
    r = max2(L[len(L)//2:]) #complexity O(nlogn)
    return max(l,r)


def max11(L,left,right):
    if left==right:
        return L[left]
    return max(L[left], max11(L,left+1,right))

def max_list11(L):
    return max11(L,0,len(L)-1) 

#-----------------------------------------

def max22(L, left, right):
    #print ("right: " , right)
    #print ("left: " , left)
    if left == right:
        #print(L[left])
        return L[left]
    middle = (right + left)//2
    #r2 = max(L[left],max22(L,middle+1,right))
    #print("right")
    #l2 = max(L[middle],max22(L,left,middle))
    #print("left")
    return max(max(L[middle],max22(L,left,middle)),max(L[left],max22(L,middle+1,right)))


def max_list22(L):
    return max22(L,0,len(L)-1)
