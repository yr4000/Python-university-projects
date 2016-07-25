###########################################################################
#                                                                         #
#   A collection of tests and timers for HW4                              #
#                                                                         #
#   To make this thing work, put this file                                #
#   in the same folder where your skeleton4.py file is and                #
#   replace "Your_skeleton_file_name" (line 28 in this file) with your    #
#   skeleton file name (for example "204838666", no need for ".py")       #
#                                                                         #
#   1 important note - The density_prime test is somewhat random          #
#   Therefore it is highly recommended to carry a more thorough           #
#   examination for that function.                                        #
#                                                                         #
#   Anyway, I'm no pro, so any feedback would be welcomed                 #
#                                                                         #
#   The file importing mechanism was copied from a tester                 #
#   by the almighty Shaked.                                               #
#   the first 3 tests were copied from another tester (unknown author)    #
#                                                                         #
#                                                                         #
#   Thank you Shaked, Your'e awesome                                      #
#                                                                         #
###########################################################################


from random import randint
from time import clock,time
import sys, itertools
sys.setrecursionlimit(8000)
from importlib import import_module
mod = import_module("skeleton4")
for func in mod.__dict__:
    if not func.startswith("_"):
        globals()[func] = mod.__dict__[func]

def test_max_list22(n = 10):
    for j in range(1,10):
        for i in range(n):
            lst = [randint(-100,100) for k in range(j)]
            if max(lst) != max_list22(lst):          
                print("False!\nExpected ", max(lst), "got ", max_list22(lst),"\n")

def max1(L):
    if len(L)==1:
        return L[0]
    return max(L[0], max1(L[1:]))

def max2(L):
    if len(L)==1:
        return L[0]
    l = max2(L[:len(L)//2])
    r = max2(L[len(L)//2:])
    return max(l,r)

def max11(L,left,right):
    if left==right:
        return L[left]
    return max(L[left], max11(L,left+1,right))

def max_list11(L):
    return max11(L,0,len(L)-1)

def timer_maximums(n = 50): # n - defines how many lists to create for the test
    average1 = 0 ; average11 = 0 ; average2 = 0 ; average22 = 0
    prev_av1 = 0 ; prev_av11 = 0 ; prev_av2 = 0 ; prev_av22 = 0
    functions = [[max1,average1,prev_av1],[max2,average2,prev_av2]\
                 ,[max_list11,average11,prev_av11],[max_list22,average22,prev_av22],]

    for j in [1000,2000,4000]:
        testers = []
        for i in range(1,n+1):
            testers.append([randint(-10000,10000) for k in range(j)])        
        print("\nAverage running time for lists of size ",j,":")
        for item in functions:
            for a in testers:
                t0 = clock()
                (item[0])(a)
                t1 = clock()
                item[1] += t1-t0
            item[1] = item[1]/n
            if item[2] != 0:
                print(str(item[0])[10:20],":",str(item[1])[:7], \
                      "  growth rate:",str(item[1]/item[2])[:4])
            else:
                print(str(item[0])[10:20],":",str(item[1])[:7])
            item[2] = item[1]
            
def change_old(amount, coins):
    coins = list(coins)
    if (amount == 0):
        return 1
    elif (amount < 0 or coins == []):
        return 0
    else:
        return change_old(amount, coins[:-1]) + change_old(amount - coins[-1], coins)

def test_change(n = 30): # n - the maximum amount of different coins available per test
    testers = []
    for i in range(2,n):
        for j in range(1,i):
            inner_lst = list({randint(1,(j+1)) for k in range(randint(0,i+1))})
            testers.append([i,inner_lst])
    for lst in testers:
        got = change_fast(lst[0],lst[1])
        expected = change_old(lst[0],lst[1])
        if got != expected :
            print("Expected :", expected, "Got :", got)
 

def findsubsets(S,m): #helper function - returns sorted subsets of size m
    a = itertools.combinations(S,m)
    b = []
    for element in a:
        b+= [list(element)]
    if len(b) == 0:
        b = [[]]
    return b

def test_choose_sets(n = 20): # n = maximum possible list length
    if sorted(choose_sets([1,2,3,4], 0)) != findsubsets([1,2,3,4],0):
        print("error in choose_sets()B")
        
    tmp = choose_sets(['a','b','c','d','e'], 4)
    tmp = sorted([sorted(e) for e in tmp])
    if tmp != findsubsets(['a','b','c','d','e'], 4):
        print("error in choose_sets()@")
            
    tmp = choose_sets([],0)
    if tmp != [[]]:
        print("error in choose_sets()!")
            
    for i in range(10): # random tests
        l = randint(0,n)
        k = randint(0,l)
        lst = [randint(-100,100) for i in range(k)]
        tmp = sorted(choose_sets(lst, k))
        validation = sorted(findsubsets(lst, k))
        if tmp != validation:
            if lst == [] and validation == [[]]:
                continue
            else:
                print("error in choose_sets()\n"\
                      ,"List = ",lst,"k = ",k,"Expected: ",validation,"Got: ",tmp)


def test_density_primes(show = False): #Using maximun and minimum values obsereved after many many iterations.
                           #This test is meant to raise errors only if your calculated values are way off.
    
    n_values = [(100,(0.013,0.017)),(200,(0.006,0.008)),(300,(0.0035,0.0065))\
                ,(400,(0.0027,0.0045)),(500,(0.002,0.004))]
    
    for item in n_values:
        density = 0
        result = 0
        for i in range(1,6):
            result = density_primes(item[0])
            density += result
        density /= 5
        if not (item[1][0] <= density <= item[1][1]):
            print("Error. For n =",item[0],"the expected density is between",item[1][0],"to",item[1][1])
            print("Got",density,"\n")
        else :
            if show:
                print("for n =",item[0],"the calculated density is ",density) 


def win_time(n,m,hlst,t):
    t0 = t
    t1 = time()
    delta = t1-t0
    if delta > 60:
        print("execution time for n =",n,"exceeded 60 seconds")
        return None
    if sum(hlst)==0:
        return True
    for i in range(m):  # for every column, i
        for j in range(hlst[i]): # for every possible move, (i,j)
            move_hlst = [n]*i+[j]*(m-i) # full height up to i, height j onwards
            new_hlst = [min(hlst[i],move_hlst[i]) for i in range(m)] # munching
            if not win_time(n,m,new_hlst,t):
                return True
    return False

def win_timer(n = 3): # Tests if for a given n value, running time exceeds 60 seconds
    t0 = time()
    win_time(n,n+3,[n]*(n+2)+[n-1],t0)

  
def run_tests():
    print(">> Running random tests...")
    print(">> Testing max_list22...")
    test_max_list22()
    print(">> Testing change_fast...")
    test_change()
    print(">> Testing choose_sets()...")
    test_choose_sets()
    print(">> Testing density_primes()...")
    test_density_primes()
    print(">> Done testing.\nExecuting timers...")
    timer_maximums()
    print()
    inp = input("Would you like to initiate a timer for munch? (enter 'y' for Yes, anything else for No")
    if inp == "y":
        print("This is a timer for the default win(n,m,[...]) function.",\
              "\nthe timer will raise an error if running time exceeds 1 minute.",\
              "\nChoose n value for win_timer (Press Enter for default value (3)) :")
        try:        
            n = int(input())
        except:
            n = 3
        win_timer(n)
    print(">> If no errors showed up, all tests passed =)")


ALL_TESTS = {
    22: dict(
        seif_string = 'Q22',
        function = max_list22,
        func_name = "max22",
        total_grade = 6,
        tests = [
            dict(args=([-12,501,1012,40,96,81,-500,200,41,7,91,456,937,163,-100,1234],), expected=1234, symbol='T22', grade=2),
            dict(args=([100],), expected=100, symbol='T22', grade=2),
            dict(args=([-12,-501,-1012,-40,-96,-81,-500,-200,-41,-7,-91,-456,-937,-163,-100,-1234],), expected=-7, symbol='T22', grade=2),
            ],
        ),
    3: dict(
        seif_string = 'Q3',
        function = change_fast,
        func_name = "change_fast",
        total_grade = 15,
        tests = [
            dict(args=(88, [1,2,5,10],), expected=1515, symbol='T3', grade=3),
            dict(args=(888, [1,2,3,4,5,6,7,8,9,10],), expected=342610317161847, symbol='T3', grade=3),
            dict(args=(888, [1],), expected=1, symbol='T3', grade=3),
            dict(args=(0, [1,2,5,10],), expected=1, symbol='T3', grade=3),
            dict(args=(3, [5,10],), expected=0, symbol='T3', grade=3),
            ],
        ),
    42: dict(
        seif_string = 'Q42',
        function = win_fast,
        func_name = "win_fast",
        total_grade = 12,
        tests = [
            dict(args=(5,6,[5,5,4,3,2,1],), expected=True, symbol='T42', grade=3),
            dict(args=(6,9,[6,6,6,6,6,6,6,6,5],), expected=True, symbol='T42', grade=3),
            dict(args=(2,8,[1,0,0,0,0,0,0,0],), expected=False, symbol='T42', grade=3),
            dict(args=(3, 4, [3,3,3,3],), expected=True, symbol='T42', grade=0),
            dict(args=(1,1,[1],), expected=False, symbol='T42', grade=0),
            dict(args=(2,12,[2,2,2,2,2,2,2,2,2,2,2,1],), expected=False, symbol='T42', grade=3),
            ],
        )
}

def run_with_limited_time(func, args=(), kwargs={}, timeout_duration=10):
    '''This function will spwan a thread and run the given function using the args, kwargs and
    return the given default value if the timeout_duration is exceeded
    '''
    import threading
    class InterruptableThread(threading.Thread):
        def __init__(self):
            threading.Thread.__init__(self)
            self.result = None
        def run(self):
            try:
                self.result = func(*args, **kwargs)
            except:
                self.result = (sys.exc_info()[0], sys.exc_info()[1])
        def stop(sefl):
            super(self)

    it = InterruptableThread()
    it.daemon = True
    it.start()
    it.join(timeout_duration)
    if it.isAlive():
        return [True, it.result]
    else:
        return [False, it.result]

def tests(n=0):
    print(">> Running tests from 2013 tester...")
    err_l = []
    err_s = []
    grade = 0

    for seif in ALL_TESTS:
        if n == 0 or seif == n or n == -1:
            function = ALL_TESTS[seif]['function']
            tests = ALL_TESTS[seif]['tests']
            seif_string = ALL_TESTS[seif]['seif_string']
            total_grade = ALL_TESTS[seif]['total_grade']
            func_name = ALL_TESTS[seif]['func_name']
            exception_symbol = "T" + seif_string[1:] + "_x"
            timeout_symbol = "T" + seif_string[1:] + "_t"
            time_to_run = ALL_TESTS[seif].get('time_to_run', 20)
            tmp_grade = 0
            tmp_errs = []

            if (n != -1):
                print("Test %s: %s: (%d)" % (func_name, seif_string, total_grade))

            for test in tests:
                reduce = False

                timeout = run_with_limited_time(function, test['args'], {}, time_to_run)
                if timeout[0]:
                    err_l.append("%s: Timeout in %s (running time was longer than %d seconds) - [%s] - (%d)\n" % (seif_string, func_name, time_to_run, timeout_symbol, test['grade']))
                    reduce = True
                    symbol = timeout_symbol
                else:
                    res = timeout[1]
                    if (isinstance(res, tuple)):
                        e = timeout[1][1]
                        err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                        reduce = True
                        symbol = exception_symbol
                    else:
                        try:
                            if res != test['expected']:
                                err_l.append("%s: Error in %s - [%s] - (%d)" % (seif_string, func_name, test['symbol'], test['grade']))
                                err_l.append("Expected: " + str(test['expected']))
                                err_l.append("Got:      " + str(res) + "\n")
                                reduce = True
                                symbol = test['symbol']
                        except:
                            e = sys.exc_info()[1]
                            err_l.append("%s: Exception in %s (%s) - [%s] - (%d)\n" % (seif_string, func_name, e, exception_symbol, test['grade']))
                            reduce = True
                            symbol = exception_symbol

                if reduce:
                    err_s.append(symbol)
                    grade -= test['grade']

    if (n != -1):
        print()
        print("\n".join(str(err) for err in err_l))
        print(grade)

    return err_s

tests()
run_tests()

