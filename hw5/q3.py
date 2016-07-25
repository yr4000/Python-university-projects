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
            
    def insert(self, key, value): #still need to be checked
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
                #print("yeaaaa!!!")
                k[1] = value #why when i tried to change the whole list it failed?
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
    words_simpledict = SimpleDict(len(set(words))) #Simpledict sounds like a lords name
    for word in words:
        if words_simpledict.find(word) == None:
            words_simpledict.insert(word,1)
        else:
            words_simpledict.insert(word,words_simpledict.find(word) +1)
    return words_simpledict
        

def sort_by_cnt(count_dict):
    return sorted(count_dict.items(), key = lambda lst: lst[1], reverse = True)
