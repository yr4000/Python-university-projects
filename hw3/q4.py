# a
def steady_state(lst):
	import math	
	n = len(lst) - 1
	index = math.floor(n/2)
	start_index = 0
	end_index = n
	while index != lst[index]:
		if index < lst[index]:
			end_index = index
			index = math.floor((index+start_index)/2)
			print("if 1")
		if index > lst[index]:
			start_index = index
			index = math.ceil((end_index+index)/2)
			print("if 2")
		if index == start_index: break
		if index == end_index: break

		print("start index: " , start_index)
		print("index: " , index)
		print("end index: " , end_index)

	print(lst)
	print(index)
	if index == lst[index]: return lst[index]
	else: return None


### d
def cnt_steady_states(lst):
        import math
        End = None
        Start = None
        end_index = len(lst) - 1
        start_index = 0
        temp_index = end_index
        
        while End != temp_index: #finding the highest equal
                if temp_index == lst[temp_index]:
                        End = temp_index
                        temp_index = math.ceil((temp_index + end_index)/2)
                        end_index = temp_index
                        print("loop 1.1")
                        continue
                if temp_index > lst[temp_index]:
                        start_index = temp_index
                        temp_index = math.ceil((end_index + start_index)/2)
                        print("loop 1.2")
                        continue
                if temp_index < lst[temp_index]:
                        end_index = temp_index
                        temp_index = math.ceil((end_index + start_index)/2)
                        print("loop 1.3")
                if temp_index == start_index: return 0
                if temp_index == end_index: return 0
                print("start index: " , start_index)
                print("temp index is " , temp_index)
                print("end index is " , end_index)

        temp_index = start_index
        while Start != temp_index:  #finding the lowest equal
                if temp_index > lst[temp_index]:
                        start_index = temp_index
                        temp_index = math.floor((start_index + end_index)/2)
                        print("loop 2.1")
                        continue
                if temp_index < lst[temp_index]:
                        return "bug"
                if temp_index == lst[temp_index]:
                        Start = temp_index
                        temp_index = math.floor((temp_index + start_index)/2)
                        start_index = temp_index
                        print("loop 2.3")
                        
        print("this is Start: " , Start)
        print("this is End: " , End)
        print(lst)
        print(len(range(Start, End+1)))
        return len(range(Start, End+1))
                        
                        
         
        
def test(): 
        
        if steady_state([-4,-1,0,3,5]) != 3 or \
        steady_state([-4,-1,2,3,5]) not in [2,3] or \
        steady_state([-4,-1,0,4,5]) != None:
                print("error in steady_state")
        
        if cnt_steady_states([-4,-1,0,3,5]) != 1 or \
        cnt_steady_states([-4,-1,2,3,5]) != 2 or \
        cnt_steady_states([-4,-1,0,4,5]) != 0:
                print("error in cnt_steady_states")
        
