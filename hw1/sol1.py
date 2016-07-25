#1st solution
import time
num = int(eval(input("Please enter a positive integer: ")))
m = num
cnt = 0
t0 = time.clock()
while m>0:
    if m%10 == 0:
      cnt = cnt+1
    m = m//10
t1 = time.clock()
print ("it took", t1-t0, "secs")
#print (num)
print (cnt)
