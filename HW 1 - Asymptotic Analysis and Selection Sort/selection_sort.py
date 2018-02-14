#!/usr/bin/env python3
#Jai Khanna
#Algorithms and Data Structures 2017
#HW 1 - Selection Sort

import random as rd
import time
import matplotlib.pyplot as plt

def main():
    t=Tools()

    x=list(range(0,10000,100))
    
    #Worst case: a reverse sorted list
    print("Computing the time taken for worst case...")
    worst=[]
    for n in x:
        A=t.genReverseSorted(n)
        worst.append(t.compTime(A))
    print("done")

    #Best case: a sorted list
    print("Computing the time taken for best case...")
    best=[]
    for n in x:
        A=t.genSorted(n)
        best.append(t.compTime(A))
    print("done")

    #Average case: a random list
    print("Computing the time taken for average case...")
    average=[]
    for n in x:
        mytime=0
        for i in range(5):
            A=t.genRandom(0,10000,n)
            mytime+=(t.compTime(A))
        mytime=mytime/5
        average.append(mytime)
    print("done")
    
    plt.plot(x,worst,'ro',label='worst')
    plt.plot(x,best,'bo',label='best')
    plt.plot(x,average,'go',label='average')
    plt.ylabel('Computation time t')
    plt.xlabel('Input size n')
    plt.legend()
    plt.show()
    
class Tools():
    def __init__(self):
        pass

    #Selection sort    
    def selectionSort(self,A):
        # Traverse through all array elements
        for i in range(len(A)):            
            # Find the minimum element in remaining 
            # unsorted array
            min_pos = i
            for j in range(i+1, len(A)):
                if A[min_pos] > A[j]:
                    min_pos = j        
            # Swap the found minimum element with 
            # the element at pos i    
            A[i], A[min_pos] = A[min_pos], A[i]
    
    #Generates a reverse sorted list n...0
    def genReverseSorted(self,n):
        A=list(range(n))
        A=list(reversed(A))
        return A

    #Generates a sorted list 0...n
    def genSorted(self,n):
        A=list(range(n))
        return A

    #Generates a random list of size n with range a,b:
    def genRandom(self,a,b,n):
        A=rd.sample(range(a,b),n)
        return A
    
    #Returns the time taken to perform selection sort function
    def compTime(self,A):
        t=Tools()
        start=time.clock()
        t.selectionSort(A)
        return time.clock() - start

if __name__ == "__main__":
	main()