import time
import random
from numpy.random import seed
from numpy.random import randint
import matplotlib.pyplot as plt

class fibExeTime():
    def __init__(self):
        self.lists = []

    def fibonacciRecursive(self,n):
        if n<=1:
            return n
        else:
            return self.fibonacciRecursive(n-1) + self.fibonacciRecursive(n-2)

    def fibonacciIteration(self,n):
        a = 0
        b = 1
        while(n-2):
            if n>0:
                c=a+b
                a,b = b,c
                n= n-1
    def fibonacciBetter(self,n):
        return self._fibonacciBetter(n)[0]

    def _fibonacciBetter(self,n):
        if n == 0:
            return (0, 1)
        else:
            a, b = self._fibonacciBetter(n >> 1)
            c = a * ((b << 1) - a)
            d = a * a + b * b
            if n & 1:
                return (d, c + d)
            else:
                return (c, d)
    def driverProgram(self):
        terms = []
        fiboRecursiveTime = []
        fiboIterationTime = []
        fiboBetterTime = []
        for i in range(0,5):
            nterm = int(input("Enter length of terms:"))
            startTime1 = time.clock()
            Fibo.fibonacciRecursive(nterm)
            endTime1 = time.clock()
            startTime2 = time.clock()
            Fibo.fibonacciIteration(nterm)
            endTime2 = time.clock()
            startTime3 = time.clock()
            Fibo.fibonacciBetter(nterm)
            endTime3 = time.clock()
            fiboRecursiveTime.append(endTime1-startTime1)
            fiboIterationTime.append(endTime2-startTime2)
            fiboBetterTime.append(endTime3-startTime3)
            terms.append(10*i*i)

        plt.xlabel('Term Length')
        plt.ylabel('Time Complexity')
        plt.plot(terms,fiboRecursiveTime,label ='Recursive')
        plt.plot(terms,fiboIterationTime,label = 'Iteration')
        plt.plot(terms,fiboBetterTime,label = 'Better')
        plt.grid()
        plt.legend()
        plt.show()



Fibo = fibExeTime()
Fibo.driverProgram()
