#!/usr/bin/env python3
#Jai Khanna
#Algorithms and Data Structures 2017
#HW 3 - Fibonacci

import time
import matplotlib.pyplot as plt
import numpy as np
from numpy import linalg as LA
import math
import decimal

S5 = decimal.Decimal(5).sqrt()
PHI = (1 + S5) / 2

def main():
    t=Tools()

    t.testFib(10)


    print("Matrix algorithm")
    matrixTime=[]
    matrix=[]
    i=decimal.Decimal(1)
    compTime=0
    while compTime<5 and i<100000:
        compTime=t.compTimeFib(t.matrixFib,i)
        if compTime<0:
            break
        print(i,' ',compTime)
        matrixTime.append(compTime)
        matrix.append(i)
        i=decimal.Decimal(math.ceil(i*decimal.Decimal(10)))
    print("finish matrix")    

    print("Naive algorithm")
    naiveTime=[]
    naive=[]
    i=1
    compTime=0
    while compTime<5:
        compTime=t.compTimeFib(t.naiveFib,i)
        print(i,' ',compTime)
        naiveTime.append(compTime)
        naive.append(i)
        i=i+1
    print("finished naive")

    print("Bottom up algorithm")
    bottomUpTime=[]
    bottomUp=[]
    i=1
    compTime=0
    while compTime<5 and i<100000:
        compTime=t.compTimeFib(t.bottomUpFib,i)
        if compTime<0:
            break
        print(i,' ',compTime)
        bottomUpTime.append(compTime)
        bottomUp.append(i) 
        i=decimal.Decimal(math.ceil(i*decimal.Decimal(10)))
    print("finish bottom up")

    print("Closed Form Algorithm")
    closedFormTime=[]
    closedForm=[]
    i=decimal.Decimal(1)
    compTime=0
    while compTime<5 and i<100000:
        compTime=t.compTimeFib(t.closedFormFib,i)
        if compTime<0:
            break
        print(i,' ',compTime)
        closedFormTime.append(compTime)
        closedForm.append(i)
        i=decimal.Decimal(math.ceil(i*decimal.Decimal(10)))
    print("finished closed form") 
    
    plt.plot(naive,naiveTime,'-bo',label='Naive Recursion')
    plt.ylabel('Computation time')
    plt.xlabel('Value of n')
    plt.legend()
    plt.show()
    plt.close()

    plt.plot(naive,naiveTime,'-bo',label='Naive Recursion')
    plt.plot(bottomUp,bottomUpTime,'-go',label='Bottom Up')
    plt.plot(closedForm,closedFormTime,'-yo',label='Closed Form')
    plt.plot(matrix,matrixTime,'-ro',label='Matrix multiplication')
    plt.ylabel('Computation time')
    plt.xlabel('Value of n')
    plt.xscale('log')
    plt.yscale('log')
    plt.legend()
    plt.show()
                
class Tools():
    def __init__(self):
        pass

    def testFib(self,n):
        t=Tools()
        n=round(n)
        print(t.bottomUpFib(n))
        print(t.naiveFib(n))
        print(t.matrixFib(n))
        print(t.closedFormFib(n))

    #computes the time taken to execute a function that determines the n'th fibonacci number
    def compTimeFib(self,f,n):
        start=time.clock()
        f(n)
        if f(n)<0:
           return -1
        return time.clock() - start

    #returns the nth fibonacci number using naive recursion
    def naiveFib(self,n):
        n=round(n)
        t=Tools()
        if n==0 or n==1:
            return n
        else:
            return t.naiveFib(n-1)+t.naiveFib(n-2)
    
    #returns the nth fibonacci number bottom up
    def bottomUpFib(self,n):
        n=round(n)
        if n==0 or n==1:
            return n
        else:
            try:
                first=decimal.Decimal(0)
                second=decimal.Decimal(1)
                final=decimal.Decimal(0)
                for _ in range(n-1):
                    final=second+first
                    first=second
                    second=final
                return final
            except Exception:
                return -1

    #returns the nth fibannaci number, computed using closed form
    def closedFormFib(self, n):
        try:
            decimal.getcontext().prec = 300
            n=round(n)
            x=decimal.Decimal(PHI**n)
            final=x/S5
            return round(final)
        except Exception:
            return -1
    
    #returns the nth fibonacci number using matrix multiplication
    def matrixFib(self, n):
        t=Tools()
        try:
            n=round(n)
            A=np.array([[1,1],[1,0]],dtype=np.float128)
            F=t.matrixPower(A,n)
            final=round(F[0][1])
            return final
        except Exception:
                return -1

    #computes matrix power to n of a square matrix
    def matrixPower(self,A,n):
        if n==0:
            return np.array([1,0],[0,1])
        if n==1:
            return A
        final=A
        for _ in range(1,n):
            final=np.matmul(final, A)
        return final
            

if __name__ == "__main__":
	main()