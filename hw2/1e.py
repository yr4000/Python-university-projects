def rotate1(lst):
    #print (id(lst))
    leng = len(lst)
    index = 0
    while index < leng - 1 :
        temp = lst[index]
        lst[index] = lst[leng - 1]
        lst[leng - 1] = temp
        index += 1
        #print ("rotation", index)
    #print (id(lst))
    return lst

def rotatek_v1(lst, k = 1):
    leng = len(lst)
    #check = 0
    if lst == []:
        #print ("empty list")
        None
    else:
        for i in range(k%leng):
            rotate1(lst)
            #check += 1
            #print ("rotation", check)
    return (lst)
        
        
