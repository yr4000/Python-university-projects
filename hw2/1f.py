def reverse_sublist(lst, start, end):
    while start < (end - 1):
        temp = lst[start]
        lst[start] = lst[end-1]
        lst[end-1] = temp
        start += 1
        end -= 1
    return lst


def rotatek_v2(lst, k):
    leng = len(lst)
   # check = 0
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
              # check += 1
              # print ("negative rotate", check)
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
               # check += 1
               # print ("positive rotate", check)
    return lst
            
   
