#Skeleton file for HW5 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

############
# QUESTION 1
############

class Polynomial():
    def __init__(self, coeffs_lst):
        self.coeffs = coeffs_lst
        
    def __repr__(self):
        terms = [" + ("+str(self.coeffs[k])+"*x^" + \
                 str(k)+")" \
                 for k in range(len(self.coeffs)) \
                 if self.coeffs[k]!=0]
        terms = "".join(terms)
        if terms == "":
            return "0"
        else:
            return terms[3:] #discard leftmost '+'

    def degree(self):
        return(len(self.coeffs) - 1)

    def evaluate(self, x):
        m_list = []
        n = len(self.coeffs) 
        temp = 1
        for i in range(n):
            if i == 0: m_list.append(temp)
            else: temp *= x ; m_list.append(temp)
        sol = 0
        for i in range(n): sol +=self.coeffs[i]*m_list[i]
        return sol
            

    def derivative(self):
        der_pol = self.coeffs[1:]
        for k in range(len(der_pol)):
            der_pol[k] = der_pol[k]*(k+1)
        if der_pol == []: der_pol = [0]
        return Polynomial(der_pol)

    def __eq__(self, other):
        assert isinstance(other, Polynomial)
        if len(self.coeffs) != len(other.coeffs):
            return False
        for i in range(len(self.coeffs)):
            if self.coeffs[i] != other.coeffs[i]:
                return False
        return True
            
    def __lt__(self, other):
        assert isinstance(other, Polynomial)  
        pass #replace this with your code
    
    def __add__(self, other): 
        assert isinstance(other, Polynomial)
        temp_self = []
        temp_other = []
        if len(self.coeffs) > len(other.coeffs):
            temp_other += other.coeffs \
                          + [0]*(len(self.coeffs) - len(other.coeffs))
            temp_self = self.coeffs
        else:
            temp_self += self.coeffs \
                          + [0]*(len(other.coeffs) - len(self.coeffs))
            temp_other = other.coeffs
        for i in range(len(temp_self)):
            temp_self[i] += temp_other[i]
        while temp_self[len(temp_self)-1] == 0:
            if temp_self == [0]: break
            temp_self = temp_self[:len(temp_self)-1]
        return Polynomial(temp_self)
        
            

    def __neg__(self):
        temp = []
        for i in range(len(self.coeffs)):
            temp += [-self.coeffs[i]]
        return Polynomial(temp)

    def __sub__(self, other):
        assert isinstance(other, Polynomial)
        temp_self = []
        temp_other = []
        if len(self.coeffs) > len(other.coeffs):
            temp_other += other.coeffs \
                          + [0]*(len(self.coeffs) - len(other.coeffs))
            temp_self = self.coeffs
        else:
            temp_self += self.coeffs \
                          + [0]*(len(other.coeffs) - len(self.coeffs))
            temp_other = other.coeffs
        for i in range(len(temp_self)):
            temp_self[i] -= temp_other[i]
        while temp_self[len(temp_self)-1] == 0:
            if temp_self == [0]: break
            temp_self = temp_self[:len(temp_self)-1]
        return Polynomial(temp_self)
                          
            

    def __mul__(self, other):
        assert isinstance(other, Polynomial)  
        temp_pol = [0]*(len(self.coeffs) + len(other.coeffs))
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                temp_pol[i+j] += self.coeffs[i]*other.coeffs[j]
        while temp_pol[len(temp_pol)-1] == 0:
            if temp_pol == [0]: break
            temp_pol = temp_pol[:len(temp_pol)-1]
        return Polynomial(temp_pol)

    def find_root(self):
        return NR(lambda x: self.evaluate(x), diff_param(lambda x: self.evaluate(x)))


## code for Newton Raphson, needed in find_root ##
from random import *

def diff_param(f,h=0.001):
    return (lambda x: (f(x+h)-f(x))/h)


def NR(func, deriv, epsilon=10**(-8), n=100, x0=None):
    if x0 is None:
        x0 = uniform(-100.,100.)
    x=x0; y=func(x)
    for i in range(n):
        if abs(y)<epsilon:
            #print (x,y,"convergence in",i, "iterations")
            return x
        elif abs(deriv(x))<epsilon:
            #print ("zero derivative, x0=",x0," i=",i, " xi=", x)
            return None
        else:
            #print(x,y)
            x = x- func(x)/deriv(x)
            y = func(x)
    #print("no convergence, x0=",x0," i=",i, " xi=", x)
    return None




############
# QUESTION 2
############

### Tree node class - code from lecture, You need to add a field ###

class Tree_node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None

    def __repr__(self):
        return "[" + str(self.left) + " " + str(self.key) + " " + \
                    str(self.val) + " " + str(self.right) + "]"

### Binary search tree - code from lecture - DO NOT CHANGE ! ###

def insert(root,key,val):
    if root==None:
        root = Tree_node(key,val)
    elif key==root.key:
        root.val = val     # update the val for this key
    elif key<root.key:
        root.left = insert(root.left,key,val)
    elif key>root.key:
        root.right = insert(root.right,key,val)
    return root

def lookup(root,key):
    if root==None:
        return None
    elif key==root.key:
        return root.val
    elif key < root.key:
        return lookup(root.left,key)
    else:
        return lookup(root.right,key)


### End code from lecture ###

# a
def weight(node):
    val_sum = 0
    return iner_weight(node, val_sum)

def iner_weight(node,val_sum):
    val_sum += node.val
    if node.right == None and node.left == None: 
        node.node_weight = val_sum
        return val_sum
    if node.right == None:
        L = iner_weight(node.left, val_sum)
        node.node_weight = max(L,node.left.node_weight)
        return L
    if node.left == None:
        R = iner_weight(node.right, val_sum)
        node.node_weight = max(R,node.right.node_weight)
        return R
    else:
        R = iner_weight(node.right, val_sum)
        L = iner_weight(node.left, val_sum)
        node.node_weight = max(L,R)
    return max(R,L)
    

# b
def heavy_path(node):
    weight(node)
    heavy_list = [node.key]
    while node.left != None or node.right != None: 
        R = node.right
        L = node.left
        if R != None and L != None:
            if R.node_weight >= L.node_weight:
                heavy_list += [R.key]
                node = R
                continue
            else:
                heavy_list += [L.key]
                node = L
        if R == None:
            heavy_list += [L.key]
            node = L
        if L == None:
            heavy_list += [R.key]
            node = R
    return heavy_list

# c
# c
def find_closest_key(node, k):
    middle = 0
    while True:
        R = node.right
        L = node.left
        if k == node.key:
            return node.key
        if k > node.key:
            if R == None: return node.key
            middle = (node.key + R.key)/2
            if middle >= k: return node.key
            else: node = R ; continue
        if k < node.key:
            if L == None: return node.key
            middle = (node.key + L.key)/2
            if middle <= k: return node.key
            else: node = L 
   



############
# QUESTION 3
############



#########################################
### SimpleDict CODE ###
#########################################

class SimpleDict:
    def __init__(self, m, hash_func=hash):
        """ initial hash table, m empty entries """      
        self.table = [ [] for i in range(m)]
        self.hash_mod = lambda x: hash_func(x) % m

    def __repr__(self):
        L = [self.table[i] for i in range(len(self.table))]
        return "".join([str(i) + " " + str(L[i]) + "\n" for i in range(len(self.table))])

    def __eq__(self, other):#for testing
        return self.table == other.table

    def items(self):
        return [item for chain in self.table for item in chain]

    def values(self):
        valist = []
        for table in self.table:
            for intable in table:
                valist += [intable[1]]
        return valist
    
    def find(self, key):
        """ returns value if key in hashtable, None otherwise  """
        if type(key) == tuple:
            for check in key: 
                if type(check) == dict or type(check) == list:
                    print("key is ILLEGAL!"); return None
            num_key = len(key)
        elif type(key)== int or type(key)== float:
            num_key = key
        elif type(key) == str:
            num_key = superord(key)
        else: print("key is ILLEGAL!"); return None
        i = self.hash_mod(num_key)
        for k in self.table[i]:
            if k[0] == key: return k[1]
        return None
            
    def insert(self, key, value): 
        """ insert an item into table
            if key already exists - update value
            key must be hashable """ 
        if type(key) == tuple:
            for check in key: 
                if type(check) == dict or type(check) == list:
                    print("key is ILLEGAL!")
                    return None
            num_key = len(key)
        elif type(key)== int or type(key)== float:
            num_key = key
        elif type(key) == str:
            num_key = superord(key)
        else: print("key is ILLEGAL!"); return None
        i = self.hash_mod(num_key)
        
        for k in self.table[i]:
            if k[0] == key:
                k[1] = value 
        if [key,value] not in self.table[i]:
            self.table[i].append([key,value])

def superord(word):
    ord_str = ""
    for i in word:
        ord_str += str(ord(i))
    ord_int = int(ord_str)
    return ord_int
        
            
#########################################
### SimpleDict CODE - end ###
#########################################

def download(url):
    ''' url should be a string containing the full path, incl. http://  '''
    f=urlopen(url)
    btext=f.read()
    text = btext.decode('utf-8')
    #read from the object, storing the page's contents in text.
    f.close()
    return text

def clean(text):
    ''' converts text to lower case, then replaces all characters except
       letters, spaces, newline and carriage return by spaces '''
    letter_set = "abcdefghijklmnopqrstuvwxyz \n\r"
    text = str.lower(text)
    cleaned = ""
    for letter in text:
        if letter in letter_set:
            cleaned += letter
        else:
            cleaned += " "
    return cleaned

def count_words_naive(words):
    count_list=[]
    words_set = set(words) #set of different words (no repetition)
    for word in words_set:
        count_list += [ [word, words.count(word)] ]
    return count_list 

def count_words(words): #need to make the list 200 slots long
    words_simpledict = SimpleDict(200) #Simpledict sounds like a lords name
    for word in words:
        if words_simpledict.find(word) == None:
            words_simpledict.insert(word,1)
        else:
            words_simpledict.insert(word,words_simpledict.find(word) +1)
    return words_simpledict
        

def sort_by_cnt(count_dict):
    return sorted(count_dict.items(), key = lambda lst: lst[1], reverse = True)


############
# QUESTION 4
############

# a
def next_row(lst):
    temp_lst = [0] +lst +[0]
    next_row = []
    for i in range(len(lst) + 1):
        next_row += [temp_lst[i] + temp_lst[i+1]]
    return next_row

# b   
def generate_pascal():
    row_i = [1]
    while True:
        yield row_i
        row_i = next_row(row_i)
        
# c
def generate_bernoulli():
    row_i = [1]
    while True:
        yield [sum(row_i[:k+1]) for k in range(len(row_i))]
        row_i = next_row(row_i)       


############
# QUESTION 5
############

##In order to test Q5 uncomment the following line
from matrix import * #matrix.py needs to be at the same directory

# a
def upside_down(im):
    n,m = im.dim()
    im2 = Matrix(n,m)
    for i in range(n):
        for k in range(m):
            im2.rows[i][k] = im.rows[n-i-1][k]
    return im2

# b
def reconstruct_image(m):
    puzzle_pieces = []
    for i in range(1,m**2+1): #create list of puzzle pieces
        puzzle_pieces.append(Matrix.load("puzzle\im{}.bitmap".format(i)))
    l,k = puzzle_pieces[0].dim()

    puzzle_columns = [] #now constructing columns
    for i in range(m): 
        totem = puzzle_pieces[0]
        puzzle_pieces.remove(totem)
        for i in range(m-1):
            for piece in puzzle_pieces: 
                RN = len(totem.rows) #number of rows in totem
                if totem.rows[0] == piece.rows[l-1]: #checks the first row
                    totem.rows = totem.rows[1:] #get rid of the extra rows
                    totem.rows = piece.rows + totem.rows
                    puzzle_pieces.remove(piece)
                    continue
                elif totem.rows[RN-1] == piece.rows[0]: #checks the last row
                    totem.rows = totem.rows[:RN -1]
                    totem.rows += piece.rows
                    puzzle_pieces.remove(piece)
                    
        puzzle_columns.append(totem)

    prize = puzzle_columns[0] #now to crack the secret! (construct the whole picture)
    puzzle_columns.remove(prize)
    RN = len(puzzle_columns[0].rows)
    for i in range(m-1):
        for column in puzzle_columns:
            CN = len(prize.rows[0]) #checks number of column in prize
            prize_l_column = [prize.rows[i][0] for i in range(RN)]
            column_r_column = [column.rows[i][k-1] for i in range(RN)]
            
            if prize_l_column == column_r_column:
                for i in range(RN):
                    prize.rows[i] = prize.rows[i][1:] #get rid of the extra columns
                    prize.rows[i] = column.rows[i] + prize.rows[i]
                puzzle_columns.remove(column)
                continue

            prize_r_column = [prize.rows[i][CN-1] for i in range(RN)]
            column_l_column = [column.rows[i][0] for i in range(RN)]
            
            if prize_r_column == column_l_column:
                for i in range(RN):
                    prize.rows[i] = prize.rows[i][:CN-1]
                    prize.rows[i] += column.rows[i]
                puzzle_columns.remove(column)
                   
    return prize




########
# Tester
########

def test():

    #Question 1
    q = Polynomial([0, 0, 0, 6])
    if str(q) != "(6*x^3)":
        print("error in Polynomial.__init__ or Polynomial.in __repr__")
    if q.degree() != 3:
        print("error in Polynomial.degree")
    p = Polynomial([3, -4, 1])
    if p.evaluate(10) != 63:
        print("error in Polynomial.evaluate")
    dp = p.derivative()
    ddp = p.derivative().derivative()
    if ddp.evaluate(100) != 2:
        print("error in Polynomial.derivative")
    if not p == Polynomial([3, -4, 1]) or p==q:
        print("error in Polynomial.__eq__")
    r = p+q
    if r.evaluate(1) != 6:
        print("error in Polynomial.__add__")
    if not (q == Polynomial([0, 0, 0, 5]) + Polynomial([0, 0, 0, 1])):
        print("error in Polynomial.__add__ or Polynomial.__eq__")
    if (-p).evaluate(-10) != -143:
        print("error in Polynomial.__neg__")
    if (p-q).evaluate(-1) != 14:
        print("error in Polynomial.__sub__")
    if (p*q).evaluate(2) != -48:
        print("error in Polynomial.__mult__")
    if (Polynomial([0])*p).evaluate(200) != 0:
        print("error in Polynomial class")
    root = p.find_root()
    if root-3 > 10**-7 and root-1 > 10**-7:
        print("error in Polynomial.find_root")


    #Question 2
    t = None
    t = insert(t, 1, 85) #the first time we change t from None to a "real" Node
    insert(t, 2.3, -30)
    insert(t, -10, 7.5)
    insert(t, 2, 10.3)
    if weight(t) != 92.5:
        print("error in weight()")
    if heavy_path(t) != [1, -10]:
        print("error in heavy path()")

    if find_closest_key(t, -5) != -10:
        print("error in find_closest_key()")
    if find_closest_key(t, 2.2) != 2.3:
        print("error in find_closest_key()")



    #Question 3  
    h = SimpleDict(200)
    h.insert("ab", 2)
    h.insert("ef", 1)
    h.insert("cd", 3)
    d = count_words(["ab", "cd", "cd", "ef", "cd", "ab"]) 
    if d is None:
        print("error in count_words()")
    elif d != h:
        print("error in count_words()")
    if sort_by_cnt(d) != [['cd', 3], ['ab', 2], ['ef', 1]]:
        print("error in sort_by_cnt()")

    
    # Question 4
    gp = generate_pascal()
    if gp == None:
        print("error in generate_pascal()")
    elif next(gp)!=[1] or next(gp)!=[1,1] or next(gp)!=[1,2,1]:
        print("error in generate_pascal()")
