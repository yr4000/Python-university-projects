#3rd solution
num = int(eval(input("Please enter a positive integer: ")))
import time
t0 = time.clock()
cnt = str.count(str(num), "0")
t1 = time.clock()
print("it haz", cnt, "zerz")
print ("it tooks", t1-t0 ,"secs")
