num = int(eval(input("Please enter a positive integer: ")))
print (len(str(num)))
newnum = ""
index = -1
lengh = 0
L_newnum = None

for dig in str(num):
    if int(dig)%2 != 0:
        newnum = newnum + dig
    elif int(dig)%2 ==0:
        if lengh < len(newnum):
              L_newnum = newnum
              lengh = len(newnum)
              index = str(num).find(L_newnum)
        newnum = "" 
       
print("The maximal length is", lengh)
print("Sequence starts at", index)
print("Sequence is", L_newnum)

