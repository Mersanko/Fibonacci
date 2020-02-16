import timeit
import matplotlib.pyplot as plt

class fibExeTime():
    def __init__(self):
        self.termslist = []
        self.nterm = 0
        self.nthTerm1 = list()
        self.nthTerm2 = list()
        self.nthTerm3 = list()
        self.exeTime1 = list()
        self.exeTime2 = list()
        self.exeTime3 = list()

    def driveProgram(self):
        self.nterm = int(input("Enter nth Term:"))
        Fibo.termsToBePlot(self.nterm)
        for i in range(0,len(self.termslist)-1):
            self.nthTerm1.append(i+1)
        for t in range(0,len(self.termslist)-1):
            self.nthTerm2.append(t+1)
        for r in range(0,len(self.termslist)-1):
            self.nthTerm3.append(r+1)

        for e in range(len(self.nthTerm1)):

            startTime1 = timeit.timeit()
            Fibo.fibonacciRecursive(e)
            endTime1 = timeit.timeit()
            self.exeTime1.append(endTime1-startTime1)

            startTime2 = timeit.timeit()
            Fibo.fibonacciRecursive(e)
            endTime2 = timeit.timeit()
            self.exeTime2.append(endTime2-startTime2)

            startTime3 = timeit.timeit()
            Fibo.fibonacciRecursive(e)
            endTime3 = timeit.timeit()
            self.exeTime3.append(endTime3-startTime3)


        plt.xlabel('Term Length')
        plt.ylabel('Time Complexity')

        plt.plot(self.nthTerm1,self.exeTime1,label ='Recursive')

        plt.plot(self.nthTerm2,self.exeTime2,label ='Iteration')

        plt.plot(self.nthTerm3,self.exeTime3,label ='Better')

        plt.grid()
        plt.legend()
        plt.show()

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
    def termsToBePlot(self,n):
            a = 0
            b = 1
            self.termslist.append(a)
            self.termslist.append(b)
            print("Fibonacci Seqeunce",end=" ")
            print(a,b,end=" ")

            while(n-2):
                if n>0:
                    c=a+b
                    self.termslist.append(c)
                    print(c,end=" ")
                    a,b = b,c
                    n= n-1

    def Sequence(self):
        self.nterm = int(input("Enter nth Term:"))
        Fibo.termsToBePlot(self.nterm)



Fibo = fibExeTime()
Fibo.driveProgram()
