num = 2**100
cnt=0
print (num)
import time
t0 = time.clock()
for i in range(num):
    cnt = cnt+1
    print (cnt)
t1 = time.clock()
print ("it took" , t1-t0, "secs")

