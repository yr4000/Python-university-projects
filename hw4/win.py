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

def win(n,m,hlst,show=False):
    ''' determines if in a given configuration, represented by hlst,
    in an n-by-m board, the player who makes the current move has a
    winning strategy. If show is True and the configuration is a win,
    the chosen new configuration is printed.'''
    
    assert n>0 and m>0 and min(hlst)>=0 and max(hlst)<=n and len(hlst)==m
    if sum(hlst)==0:
       # print("------")
        return True
    for i in range(m):  # for every column, i
       # print("tree" , i)
        for j in range(hlst[i]): # for every possible move, (i,j)
            move_hlst = [n]*i+[j]*(m-i) # full height up to i, height j onwards
           # print(move_hlst)
            new_hlst = [min(hlst[i],move_hlst[i]) for i in range(m)] # munching
           # print("***", new_hlst)
            if not win(n,m,new_hlst):
                #print("woogle-moogle")
                if show: #what does that means???
                    print(new_hlst)
                return True
    return False

def win_fast(n,m,hlst,show=False):
    mem = {}
    return iner_win_fast(n, m, hlst, mem)

def iner_win_fast(n, m, hlst,mem, show=False):
    assert n>0 and m>0 and min(hlst)>=0 and max(hlst)<=n and len(hlst)==m
    #print(mem)
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
    
