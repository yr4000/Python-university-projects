def f1(lst):
    n = len(lst)
    for i in range(n):
        lst.extend(range(i))
       # print ("this is range", range(i))
       # print (lst)


def f2(lst):
    n = len(lst)
    for i in range(n):
        lst.extend(range(len(lst)))
        print ("this is range: ", range(len(lst)))
        print (lst)

def f3(lst):
    n = len(lst)
    for i in range(n):
        lst = lst + list(range(len(lst)))
        print ("this is range: " , range(len(lst)))
        print (lst)

def f4(lst):
    n = len(lst)
    for i in range(n):
        lst.extend(range(len(lst), len(lst)+10000))
        print (len(lst))
