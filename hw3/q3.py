def multi_merge_v1(lst_of_lsts):
    all = [e for lst in lst_of_lsts for e in lst]
    merged = []
    while all != []:
        minimum = min(all)
        merged += [minimum]
        all.remove(minimum)
    return merged

def multi_merge_v2(lst_of_lsts):
        i = 0
        copy_lst = []
        for lst in lst_of_lsts:
            copy_lst += [[e for e in lst_of_lsts[i]]]
            i += 1
        print (copy_lst)
        temp_min = []
        sorted_list = []
        i = 0
        for lst in copy_lst:
                temp_min += [copy_lst[i][0]]
                i += 1
        while temp_min != []:
        	minimum = min(temp_min)
        	sorted_list += [minimum]
        	index = temp_min.index(minimum)
        	copy_lst[index].remove(minimum)
        	if copy_lst[index] != []: temp_min[index] = copy_lst[index][0]
        	else: temp_min.remove(minimum) ; copy_lst.remove(copy_lst[index])
        	print ("this is temp_min " , temp_min)		
        	print (sorted_list)

        return sorted_list



def merge(lst1, lst2):
    """ merging two ordered lists using
        the two pointer algorithm """
    n1 = len(lst1)
    n2 = len(lst2)
    lst3 = [0 for i in range(n1 + n2)]  # alocates a new list
    i = j = k = 0  # simultaneous assignment
    while (i < n1 and j < n2):
        if (lst1[i] <= lst2[j]):
            lst3[k] = lst1[i]
            i = i +1
        else:
            lst3[k] = lst2[j]
            j = j + 1
        k = k + 1  # incremented at each iteration
    lst3[k:] = lst1[i:] + lst2[j:]  # append remaining elements
    return lst3


def multi_merge_v3(lst_of_lsts):
	m = len(lst_of_lsts)
	merged = []
    
	for lst in lst_of_lsts:
		merged = merge(merged, lst)

	return merged		        
		

