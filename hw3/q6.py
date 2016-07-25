def sort_num_list(lst):
    k = int(max([i**2 for i in lst])**0.5)
    z_lst = 4*k*[0] +[0]
    sorted_lst = []
    i = 0
    for num in lst:
        index = int((num + k)*2)
        z_lst[index] += 1
       # print ("this is z_lst " , z_lst)
    for num in z_lst:
        sorted_lst += z_lst[i]*[i*0.5 - k]
        i += 1
       # print("this is sorted_lst: " , sorted_lst)

    return sorted_lst
    
        
    
