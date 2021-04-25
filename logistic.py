import math
import matplotlib.pyplot as plt
import numpy as np
import argparse 

parser = argparse.ArgumentParser()

parser.add_argument("-a", type=float, default = 1.0)
parser.add_argument("-x", type=float, default= 0.1)
args = parser.parse_args()
a = args.a
x = args.x
def logistic( a, x,i = 0):
    if x == 0:
        return 0
    if x == float('-inf'):
        x  = 0.1
        i+=1
        return logistic(a,logistic(a,x, i=i))
    else:
        x =  a * x * (1-x)
        plt.plot(i,x, 'o-')
        plt.pause(0.01)
        plt.savefig('figs/_a_'+str(i)+'.png')
        i+=1
        if(i%2 == 0):
            a+=0.1
            print(a,x)
        if x < 0:
            x  = 0.1
            i+=1
            return logistic(a,logistic(a,x, i=i))
        else :
            return logistic(a,logistic(a,x, i=i))

logistic(a,x)
plt.show()