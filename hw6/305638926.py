#Skeleton file for HW6 - Spring 2015 - extended intro to CS

#Add your implementation to this file

#You may add other utility functions to this file,
#but you may NOT change the signature of the existing ones.

#Change the name of the file to your ID number (extension .py).

from matrix import *


############
# QUESTION 1
############

def fingerprint(mat):
    assert isinstance(mat,Matrix)
    k,makesure = mat.dim()
    assert k==makesure

    return sum(mat[i,j] for i in range(k) for j in range(k))

def move_right(mat, i, j, k, fp):
    less = 0
    more = 0
    for s in range(k):
        less += mat[i+s,j]
        more += mat[i+s,j+k]
    return fp -less +more


def move_down(mat, i, j, k, fp):
    less = 0
    more = 0
    for s in range(k):
        less += mat[i,j+s]
        more += mat[i+k,j+s]
    return fp -less +more

    
def has_repeating_subfigure(mat, k): 
    m,n = mat.dim()
    fp = fingerprint(mat[0:k,0:k])
    fp_lst = {fp:0}
    for j in range(0,n-k):
        fp = move_right(mat,0,j,k,fp)
        if fp in fp_lst: return True
        else: fp_lst[fp] = 0
    for i in range(0,m-k):
        fp = fingerprint(mat[i:k+i,0:k])
        fp = move_down(mat,i,0,k,fp)
        if fp in fp_lst: return True
        else: fp_lst[fp] = 0
        for j in range(0,n-k):
            fp = move_right(mat,i,j,k,fp)
            if fp in fp_lst: return True
            else: fp_lst[fp] = 0
    return False
            
    



########
# Tester
########

def test():
    #Question 1
    im = Matrix.load("./sample.bitmap")
    k = 2
    if fingerprint(im[:k,:k]) != 384 or \
       fingerprint(im[1:k+1,1:k+1]) != 256 or \
       fingerprint(im[0:k,1:k+1]) != 511:
        print("error in fingerprint()")
    if move_right(im, 0, 0, k, 384) != 511:
        print("error in move_right()")
    if move_down(im, 0, 1, k, 511) != 256:
        print("error in move_down()")
    if has_repeating_subfigure(im, k) != True or\
       has_repeating_subfigure(im, k=3) != False:
        print("error in repeating_subfigure()")
