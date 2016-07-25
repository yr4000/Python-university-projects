
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
        sol = 0
        for k in range(len(self.coeffs)):
            sol += self.coeffs[k]*(x**k)
        return sol

    def derivative(self):
        der_pol = self.coeffs[1:]
        for k in range(len(der_pol)):
            der_pol[k] = der_pol[k]*(k+1)
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
    
    def __add__(self, other): # how come it doesn't change the org list? cuz of +
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
        return Polynomial(temp_self)
                          
            

    def __mul__(self, other):
        assert isinstance(other, Polynomial)  
        temp_pol = [0]*(len(self.coeffs) + len(other.coeffs))
        for i in range(len(self.coeffs)):
            for j in range(len(other.coeffs)):
                temp_pol[i+j] += self.coeffs[i]*other.coeffs[j]
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
