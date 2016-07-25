def sum_divisors(n):
    divisors_list = []
    k = 2
    result = n
   # cnt = 0
   
    if k <= result: divisors_list.extend([1])
    
    while k < result:
        result = int(n/k)
        if n%k == 0 and k not in divisors_list:
            divisors_list.extend([k])
        if n%k == 0 and result not in divisors_list: #better split them in case k = result
            divisors_list.extend([result])
        k +=1
       # cnt += 1
       # print ("iteration" , cnt)
        
   # print (divisors_list)
    return sum(divisors_list)
            

def is_finite(n):
    sum = sum_divisors(n)
    print (sum)
    loop_check = n
    print(loop_check)
    while sum != loop_check: # not working for 1
        if sum == 0: break
        loop_check = sum_divisors(loop_check)
        sum = sum_divisors(sum)
        print ("loop", loop_check)
        print ("sum", sum)
        
    if sum == 0: bool = True
    if sum == loop_check: bool = False
    return bool

def cnt_finite(limit):
    cnt = 0
    for i in range(limit + 1):
        if is_finite(i) == True: cnt += 1
        else: None
       # print (i)

    return cnt

