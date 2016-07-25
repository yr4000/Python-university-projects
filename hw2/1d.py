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
        
    

