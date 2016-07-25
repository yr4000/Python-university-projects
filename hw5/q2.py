
### Tree node class - code from lecture, You need to add a field ###

class Tree_node():
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.left=None
        self.right=None
        self.node_weight = 0
        

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

a = Tree_node(1,85)
b = Tree_node(-10,7.5)
c = Tree_node(2.3,-30)
d = Tree_node(2,10.3)
a.left = b
a.right = c
c.left = d
e = Tree_node(7,50)

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
    while node.left != None or node.right != None: #the problem was an and instead of or...
        print (node.key)
        R = node.right
        L = node.left
        if R != None and L != None:
            if R.node_weight >= L.node_weight:
                print("א1")
                heavy_list += [R.key]
                node = R
                continue
            else:
                print("א2")
                heavy_list += [L.key]
                node = L
        if R == None:
            print ("ב")
            heavy_list += [L.key]
            node = L
        if L == None:
            print("ג")
            heavy_list += [R.key]
            node = R
    return heavy_list
        

# c
def find_closest_key(node, k):
    middle = 0
    while True:
        R = node.right
        L = node.left
        print ("this is node.key: " , node.key)
        if k == node.key:
            return node.key
        if k > node.key:
            if R == None: print("a1"); return node.key
            middle = (node.key + R.key)/2
            if middle >= k: print("a2"); return node.key
            else: node = R ; print("change 1"); continue
        if k < node.key:
            if L == None: print("b1"); return node.key
            middle = (node.key + L.key)/2
            if middle <= k: print("b2"); return node.key
            else: node = L ; print("change 2")
        












            
            




    
