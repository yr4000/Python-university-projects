#Skeleton file for HW2 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

############
# QUESTION 1
############

# 1c
def reverse_sublist(lst, start, end):
    while start < (end - 1):
        temp = lst[start]
        lst[start] = lst[end-1]
        lst[end-1] = temp
        start += 1
        end -= 1

# 1d
def rotate1(lst):
    leng = len(lst)
    index = 0
    while index < leng - 1 :
        temp = lst[index]
        lst[index] = lst[leng - 1]
        lst[leng - 1] = temp
        index += 1

# 1e
def rotatek_v1(lst, k = 1):
    leng = len(lst)
    if lst == []:
        None
    else:
        for i in range(k%leng):
            rotate1(lst)
    return (lst)
        

# 1f
def rotatek_v2(lst, k):
    leng = len(lst)
    if k < 0:  
        for i in range (-k):
            start = 0
            end = 2
            cnt = 0
            while cnt < leng - 1:
               reverse_sublist(lst, start, end)
               start += 1
               end += 1
               cnt += 1
    else:
        for i in range(k):
            start = leng - 2
            end = leng
            cnt = 0
            while cnt < leng -1:
                reverse_sublist(lst, start, end)
                start -= 1
                end -= 1
                cnt += 1
    return lst
            

############
# QUESTION 2b
############

def power_new(a,b):
    """ computes a**b using iterated squaring """
    result = 1
    b_bin = bin(b)[2:]
    reverse_b_bin = b_bin[: :-1]
    for bit in reverse_b_bin: 
        if bit == "1":
            result = result*a
        a = a*a
    return result


############
# QUESTION 3b
############

def add_hex(A,B):
    hex_str = "0123456789abcdef"

    if len(A) < len(B): # here we pud with zeroes
        A = A.zfill(len(B))
    else:
        B = B.zfill(len(A))
    
    rev_A = A[::-1] 
    rev_B = B[::-1]

    k = 0
    remember_1 = 0
    result = ""
    
    for i in rev_A:
        valhex_A = hex_str.index(i) # this is the hex value of i in A (int)
        indx_A = rev_A.index(i , k) # this is the index value of i in A (int)
        indx_B  = rev_B[indx_A] # this is the part of B we should sum to i (str)
        valhex_B = hex_str.index(indx_B) #this is the hex value of indx_B (int)

        temp_rslt = (valhex_A + valhex_B + remember_1) % 16 
        tmp_hex = hex_str[temp_rslt] # this str is an hex value of temp_rslt
        result = result + tmp_hex 
  
        if (valhex_A + valhex_B + remember_1) >= 16:
            remember_1 = 1

        else:
            remember_1 = 0

        k += 1 # in case the same value appears twice

    if remember_1 == 1: # in case we have a leftover 1 at the end
        str_remem_1 = "1"
        result = result + str_remem_1

    result = result[::-1]
    return result



############
# QUESTION 4b
############

def sum_divisors(n):
    divisors_list = []
    k = 2
    result = n
   
    if k <= result: divisors_list.extend([1])
    
    while k < result:
        result = int(n/k)
        if n%k == 0 and k not in divisors_list:
            divisors_list.extend([k])
        if n%k == 0 and result not in divisors_list: #better split them in case k = result
            divisors_list.extend([result])
        k +=1

    return sum(divisors_list)
            

def is_finite(n):
    sum_list = []
    sum = sum_divisors(n)
    while sum not in sum_list:
        if sum == 0: break
        sum_list.append(sum)
        sum = sum_divisors(sum)
        
    if sum == 0: bool = True
    if sum != 0: bool = False
    return bool

def cnt_finite(limit):
    cnt = 0
    for i in range(1, limit + 1):
        if is_finite(i) == True: cnt += 1
        else: None

    return cnt




############
# QUESTION 5
############

def altsum_digits(n, d):
    str_n = str(n)
    dig_sum = 0
    for i in range (d): # calculate the first sum
        dig_sum += ((-1)**i)*int(str_n[i])

    temp_sum = dig_sum  
    k = 0
    left_number = 0
    right_number = 0
    
    for num in str_n:
        if (d+k) >= len(str_n): break
        left_number = int(str_n[k])
        right_number = int(str_n[d + k])*(-1)**((d%2)+1)
        temp_sum = (-1)*(temp_sum - left_number) + right_number
        if temp_sum > dig_sum:
            dig_sum = temp_sum
        k += 1
       
    return dig_sum
            

    
    
########
# Tester
########

def test():

    lst = [1,2,3,4,5]
    reverse_sublist (lst,0,4)
    if lst != [4, 3, 2, 1, 5]:
        print("error in reverse_sublist()")        
    lst = ["a","b"]
    reverse_sublist (lst,0,1)
    if lst != ["a","b"]:
        print("error in reverse_sublist()")        

    lst = [1,2,3,4,5]
    rotate1(lst)
    if lst != [5,1,2,3,4]:
        print("error in rotate1()")        

    lst = [1,2,3,4,5]
    rotatek_v1(lst,2)
    if lst != [4,5,1,2,3]:
        print("error in rotatek_v1()")        
    
    lst = [1,2,3,4,5]
    rotatek_v2(lst,2)
    if lst != [4,5,1,2,3]:
        print("error in rotatek_v2()")        

    if power_new(2,3) != 8:
        print("error in power_new()")

    if add_hex("a5","17")!="bc":
        print("error in add_hex()")
    
    if sum_divisors(6)!=6 or \
       sum_divisors(4)!=3:        
        print("error in sum_divisors()")

    if is_finite(6) or \
       not is_finite(4):
        print("error in is_finite()")

    if cnt_finite(6) != 5:
        print("error in cnt_finite()")
        
    if altsum_digits(5**36,12)!=18:
        print("error in altsum_digits()")        
