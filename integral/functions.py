from math import log
def function(x):
    return x*x


def midle_squares(n, a, b):
    integral = 0
    h = (b-a)/n
    for i in range(n):
        current = a + (h/2)
        func = function(current)
        integral += func
        a += h
    integral *= h

    return integral


def trapeze(n, a, b):
    integral = 0
    h = (b-a)/n
    integral = (function(a) + function(b))/2
    for i in range(n-1):
        a += h
        integral += function(a)
    integral *= h
    
    return integral


def three_eight(n, a, b):
    t = s = 0
    integral = 0
    h = (b-a)/n
    f0 = function(a)
    fn = function(b)
    #print(f0,fn)
    for i in range(1,n):
        #print('i', i)
        a += h
        if i % 3 == 0:
            t += function(a)
            #print('t: ', t)
        else:
            s += function(a)
            #print('s:', s)

    integral = (3*h*(f0 + fn + 2*t + 3*s))/8
    return integral

def parabola(n, a, b):
    f_ch = f_nch = 0
    f0 = function(a)
    fn = function(b)
    integral = 0
    h = (b-a)/(2*n)
    f1 = f0 + fn
    for i in range(1,n):
        a += h
        if i % 2 == 0:
            f_ch += function(a)
        else:
            f_nch += function(a)
            
    integral = f1 + 2*f_ch + 4*f_nch
    return integral
            
    
    
            
        
        
        
    
    
    
if __name__ == '__main__':
    print(three_eight(99,0,3))
    
    print(midle_squares(40,2,5))
    print(trapeze(3,2,5))













    

