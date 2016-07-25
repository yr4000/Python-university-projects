def altsum_digits(n, d):
    str_n = str(n)
    dig_sum = 0
    for i in range (d): # calculate the first sum
        dig_sum += ((-1)**i)*int(str_n[i])

   # print("dig_sum is", dig_sum)

    temp_sum = dig_sum  
    k = 0
    left_number = 0
    right_number = 0
    
    for num in str_n:
        if (d+k) >= len(str_n): break
        left_number = int(str_n[k])
        right_number = int(str_n[d + k])*(-1)**((d%2)+1)
       # print("left_number is", left_number)
       # print("right_number is" , right_number)
        temp_sum = (-1)*(temp_sum - left_number) + right_number
       # print("temp_sum is", temp_sum)
        if temp_sum > dig_sum:
            dig_sum = temp_sum
        k += 1
       # print("SIM LEV KAN!!!dig_sum is ", dig_sum)
       
    return dig_sum
            
    
    
