def reverse_sublist(lst, start, end):
    while start < (end - 1):
        temp = lst[start]
        lst[start] = lst[end-1]
        lst[end-1] = temp
        start += 1
        end -= 1
    return lst
    
