#Skeleton file for HW4 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).


############
# QUESTION 1
############

def max22(L, left, right):
    if left == right:
        return L[left]
    middle = (right + left)//2
    return max(max(L[middle],max22(L,left,middle)),max(L[left],max22(L,middle+1,right)))


def max_list22(L):
    return max22(L,0,len(L)-1)


############
# QUESTION 2
############
def change_fast(amount, coins):
    dic_coins = {}
    return iner_change_fast(amount, coins, dic_coins)

def iner_change_fast(amount, coins, dic_coins):
    coins.sort()
    temp_tup = tuple([amount] + coins)
    if (amount < 0 or coins == []):
        return 0
    if coins == [1]:
        return 1
    if (amount == 0):
        return 1
    if temp_tup not in dic_coins:
        dic_coins[temp_tup] = iner_change_fast(amount, coins[:-1],dic_coins)\
                              + iner_change_fast(amount - coins[-1], coins,dic_coins)
    return dic_coins[temp_tup]


############
# QUESTION 3
############
def win_fast(n,m,hlst,show=False):
    mem = {}
    return iner_win_fast(n, m, hlst, mem)

def iner_win_fast(n, m, hlst,mem, show=False):
    assert n>0 and m>0 and min(hlst)>=0 and max(hlst)<=n and len(hlst)==m
    tup_hlst = tuple(hlst)
    if tup_hlst not in mem: 
        if sum(hlst)==0:
            mem[tup_hlst] = True
            return True
        for i in range(m):  # for every column, i
            for j in range(hlst[i]): # for every possible move, (i,j)
                move_hlst = [n]*i+[j]*(m-i) # full height up to i, height j onwards
                new_hlst = [min(hlst[i],move_hlst[i]) for i in range(m)] # munching
                if not iner_win_fast(n,m,new_hlst,mem):
                    if show: 
                        print(new_hlst)
                    mem[tup_hlst] = True
                    return True
        mem[tup_hlst] = False
        return False
    else:
        return mem[tup_hlst]


############
# QUESTION 4
############
def choose_sets (lst,k):
    if lst == []:
        return [[]]
    lst_of_lsts = []
    side_lst = []
    org_k = k
    return iner_choose_sets(lst_of_lsts,lst, k)
    

def iner_choose_sets(lst_of_lsts, lst, k):
    if k == 0:
        return [lst_of_lsts]
    if len(lst) == k:
        return [lst_of_lsts + lst]
    return iner_choose_sets(lst_of_lsts + [lst[0]], lst[1:], k-1)\
           + iner_choose_sets(lst_of_lsts, lst[1:], k)



############
# QUESTION 5
############

import random

def is_prime(m,show_witness=False,sieve=False):
    """ probabilistic test for m's compositeness 
    adds a trivial sieve to quickly eliminate divisibility
    by small primes """
    if sieve:
        for prime in [2,3,5,7,11,13,17,19,23,29]:
            if m % prime == 0:
                return False
    for i in range(0,100):
        a = random.randint(1,m-1) # a is a random integer in [1..m-1]
        if pow(a,m-1,m) != 1:
            if show_witness:  # caller wishes to see a witness
                print(m,"is composite","\n",a,"is a witness, i=",i+1)
            return False
    return True
        

def density_primes(n, times=10000):
    cnt_prime = 0
    if n <= 0:
        return ("YOU FOOL!!!")
    for i in range(times):
        num = random.randint(2**n ,2**(n+1)-1)
        optimus_prime = is_prime(num)
        if optimus_prime:
            cnt_prime +=1
    return cnt_prime/times







   

########
# Tester
########

def test():

    # Q1 basic tests

    if max_list22([1,20,3]) != 20:
        print("error in max22()")
    if max_list22([1,20,300,400]) != 400:
        print("error in max22()")
        
    # Q2 basic tests
    if change_fast(10, [1,2,3]) != 14:
        print("error in change_fast()")

    # Q3 basic tests
    if win_fast(3, 4, [3,3,3,3]) != True:
        print("error in win_fast()")
    if win_fast(1, 1, [1]) != False:
        print("error in win_fast()")

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
