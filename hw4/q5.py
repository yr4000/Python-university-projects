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

def bin_to_string(string):
    rev_str = string[::-1]
    bin_num = 0
    cnt = 0
    for i in rev_str:
        if i == "1":
            bin_num += 2**cnt
        cnt +=1
    return bin_num

        

def density_primes(n, times=10000):
    cnt_prime = 0
    if n <= 0:
        return ("YOU FOOL!!!")
    for i in range(times):
        num = random.randint(2**n ,2**(n+1)-1)
        optimus_prime = is_prime(num)
        if optimus_prime:
            cnt_prime +=1
   # print("cnt_prime: " ,cnt_prime)
   # print("times: " , times)
    return cnt_prime/times

def old_density_primes(n, times=10000):
    cnt_prime = 0
    if n == 0:
        return ("YOU FOOL!!!")
    for i in range(times):
        bin_str = "1"
        for i in range(n-1):
            zerone = random.randint(0,1)
            bin_str += str(zerone)
        bin_num = bin_to_string(bin_str)
       # print(bin_num)
        optimus_prime = is_prime(bin_num)
        if optimus_prime:
            cnt_prime +=1
    print(cnt_prime)
    return cnt_prime/times
    
    
        
    
