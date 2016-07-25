#question 3
file_in = open("our_input.txt","r")
file_out = open("output.txt","w") 
# i wanted the file to be sent to a specific folder. clearly you can send it anywhere the user wish to.
for line in file_in:
               #print(line)
               temp = line.split() #for temporary
               #print (temp)
               x = len(temp)
               x = str(x)
               #print (x)
               #print (type(x))
               file_out.write(x+'\n')
               #file_out.write("test")
file_out.close()
file_in.close()
    
