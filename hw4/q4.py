
def choose_sets (lst,k):
    if lst == []:
        return [[]]
    lst_of_lsts = []
    side_lst = []
    org_k = k
    return iner_choose_sets(lst_of_lsts,lst, k)
    

def iner_choose_sets(lst_of_lsts, lst, k):
    #print("lst: ", lst)
    #print("lst_of_lsts: ", lst_of_lsts)
    if k == 0:
        #print("zero")
        return [lst_of_lsts]
    if len(lst) == k:
        #print("lst==k")
        return [lst_of_lsts + lst]
    return iner_choose_sets(lst_of_lsts + [lst[0]], lst[1:], k-1)\
           + iner_choose_sets(lst_of_lsts, lst[1:], k)


def test():
    # Q4 basic tests
    if choose_sets([1,2,3,4], 0) != [[]]:
        print("error in choose_sets()")
    tmp = choose_sets(['a','b','c','d','e'], 4)
    if tmp == None:
        print("error in choose_sets()")
    else:
        tmp = sorted([sorted(e) for e in tmp])
        if tmp != [['a', 'b', 'c', 'd'], ['a', 'b', 'c', 'e'], ['a', 'b', 'd', 'e'], ['a', 'c', 'd', 'e'], ['b', 'c', 'd', 'e']]:
            print("error in choose_sets()")      
    
    
        
            
    
