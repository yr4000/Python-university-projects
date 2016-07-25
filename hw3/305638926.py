#Skeleton file for HW3 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

############
# QUESTION 2
############

def find_root(f, a, b, EPS=0.001):
    if (f(a)>0 and f(b)>0) or (f(a)<0 and f(b)<0):
       # print("YOU LIAR!!!!")
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

    return c


############
# QUESTION 3
############

# b
def multi_merge_v2(lst_of_lsts):
        i = 0
        copy_lst = []
        for lst in lst_of_lsts:
            copy_lst += [[e for e in lst_of_lsts[i]]]
            i += 1
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

# c
def multi_merge_v3(lst_of_lsts):
	m = len(lst_of_lsts)
	merged = []
    
	for lst in lst_of_lsts:
		merged = merge(merged, lst)

	return merged	



############
# QUESTION 5
############

# a
def steady_state(lst):
	import math	
	n = len(lst) - 1
	index = math.floor(n/2)
	start_index = 0
	end_index = n
	while index != lst[index]:
		if index < lst[index]:
			end_index = index
			index = math.floor((index+start_index)/2)
		if index > lst[index]:
			start_index = index
			index = math.ceil((end_index+index)/2)
		if index == start_index: break
		if index == end_index: break

		
	if index == lst[index]: return lst[index]
	else: return None


### d
def cnt_steady_states(lst):
        import math
        End = None
        Start = None
        end_index = len(lst) - 1
        start_index = 0
        temp_index = end_index
        
        while End != temp_index: #finding the highest equal
                if temp_index == lst[temp_index]:
                        End = temp_index
                        temp_index = math.ceil((temp_index + end_index)/2)
                        end_index = temp_index
                        continue
                if temp_index > lst[temp_index]:
                        start_index = temp_index
                        temp_index = math.ceil((end_index + start_index)/2)
                        continue
                if temp_index < lst[temp_index]:
                        end_index = temp_index
                        temp_index = math.floor((end_index + start_index)/2)
                        
                if temp_index == start_index: return 0
                if temp_index == end_index: return 0


        temp_index = start_index
        while Start != temp_index:  #finding the lowest equal
                if temp_index > lst[temp_index]:
                        start_index = temp_index
                        temp_index = math.floor((start_index + end_index)/2)
                        continue
                if temp_index < lst[temp_index]:
                        return "bug"
                if temp_index == lst[temp_index]:
                        Start = temp_index
                        temp_index = math.floor((temp_index + start_index)/2)
                        start_index = temp_index

        return len(range(Start, End+1))



############
# QUESTION 6
############
def sort_num_list(lst):
    k = int(max([i**2 for i in lst])**0.5)
    z_lst = 4*k*[0] +[0]
    sorted_lst = []
    i = 0
    for num in lst:
        index = int((num + k)*2)
        z_lst[index] += 1
    for num in z_lst:
        sorted_lst += z_lst[i]*[i*0.5 - k]
        i += 1

    return sorted_lst
    



   
    
########
# Tester
########

def test():
    
    f1 = lambda x : x - 1
    res = find_root(f1 , -10, 10)
    EPS=0.001
    if res == None or abs(f1(res)) > EPS  or \
       find_root(lambda x : x**2  , -10, 10) != None:
        print("error in find_root")
        
   
    if multi_merge_v2([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v2")

    if multi_merge_v3([[1,2,2,3],[2,3,5],[5]]) != [1, 2, 2, 2, 3, 3, 5, 5] :
        print("error in multi_merge_v3")

    if steady_state([-4,-1,0,3,5]) != 3 or \
       steady_state([-4,-1,2,3,5]) not in [2,3] or \
       steady_state([-4,-1,0,4,5]) != None:
        print("error in steady_state")
        
    if cnt_steady_states([-4,-1,0,3,5]) != 1 or \
       cnt_steady_states([-4,-1,2,3,5]) != 2 or \
       cnt_steady_states([-4,-1,0,4,5]) != 0:
        print("error in cnt_steady_states")

    if sort_num_list([10, -2.5, 0, 12.5, -30, 0]) \
       != [-30, -2.5, 0, 0, 10, 12.5]:
        print("error in sort_num_list")
