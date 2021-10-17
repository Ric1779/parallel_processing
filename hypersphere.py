import random
import math
import matplotlib.pyplot as plt
import functools

def hypersphere(n,d):
    a = []
    nc = 0

    a = [[random.uniform(-1,1) for i in range(d)] for j in range(n)]

    a = [list(map(lambda x: x*x,i)) for i in a]

    a = [functools.reduce(lambda x,y : x+y,i) for i in a]
    
    a = list(filter(lambda x:x<1,a))

    nc = len(a)
    
    V = (nc/n)*math.pow(2,d)

    print('n-dimensional area of {}-dimensional ball using {} points : {}'.format(d,n,V))

    Vd = math.pow(math.pi,d/2)/math.gamma((d/2)+1)
    
    print('Volume of {}-dimensional ball: {}'.format(d,Vd))

def main():
    a = [[100000,5],[100000,11]]

    for n,d in a:
        hypersphere(n,d)

if __name__ == "__main__":
    main()