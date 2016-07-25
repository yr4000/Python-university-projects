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
        
            
        
            
            
        
        
        
    
    
