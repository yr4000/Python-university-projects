def altsum_digits(n, d):
    str_n = str(n)
    sum_dig = 0
    for i in range (d): 
        sum_dig += int(str_n[i])

    print("sum_dig is", sum_dig)

    sum_start = 0
    sum_end = 0
    k = 0
    
   # print (len(str_n))
   # print (d + k)
    
    for num in str_n:
        if (d+k) >= len(str_n): break
        sum_start += int(num)
        print ("sum_start is " , sum_start)
        sum_end += int(str_n[d + k])
        print ("sum_end is " , sum_end)
        sum_temp = sum_end - sum_start
        print ("sum_temp is " , sum_temp)
        if sum_dig + sum_temp >= sum_dig:
            sum_dig = sum_dig + sum_temp
            print ("current sum dig: " , sum_dig)
            sum_start = 0
            sum_end = 0
        k += 1
            
    return sum_dig
            
    
    
