num = int(eval(input("Please enter a positive integer: ")))
import time
#2nd solution
cnt = 0
snum = str(num)
t0 = time.clock()
for digit in snum:
    if digit == "0":
        cnt = cnt+1
t1 = time.clock()
print ("it takes", t1-t0, "secs")
print (cnt, "zeroz")
