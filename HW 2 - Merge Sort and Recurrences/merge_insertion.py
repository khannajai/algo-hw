#!/usr/bin/env python3
#Jai Khanna
#Algorithms and Data Structures 2017
#HW 2 - Merge Sort

import random as rd
import time
import matplotlib.pyplot as plt

def main():
    t=Tools()
    t.generateplots(1000)

class Tools():

    def __init__(self):
        pass

    #shows computation times for different values of k when input size is n
    def generateplots(self, n):
        t=Tools()
        kvalues=list(range(5,n-10,10))

        #average case
        A=t.genRandom(n)
        mergeAvg=[]
        for k in kvalues:
            mytime=0
            for _ in range(5):
                mytime+=t.mergecompTime(A,k)
            mytime=mytime/5
            mergeAvg.append(mytime)
        plt.plot(kvalues, mergeAvg, '-bo',label='average case time for n='+str(n))

        #worst case
        A=t.genReverseSorted(n)
        mergeWorst=[]
        for k in kvalues:
            mytime=t.mergecompTime(A,k)
            mergeWorst.append(mytime)
        plt.plot(kvalues, mergeWorst, '-ro',label='worst case time for n='+str(n))

        #best case
        A=t.genSorted(n)
        mergeBest=[]
        for k in kvalues:
            mytime=t.mergecompTime(A,k)
            mergeBest.append(mytime)
        plt.plot(kvalues, mergeBest, '-go',label='best case time for n='+str(n))


        plt.ylabel('Computation time t')
        plt.xlabel('Value of k')
        plt.legend()
        plt.show()

    def insertionSort(self,A):
        for i in range(1, len(A)):
            key = A[i]
            j = i-1
            while j >=0 and key < A[j]:
                    A[j+1] = A[j]
                    j -= 1
            A[j+1] = key
        return A

    def mergeSort(self, A, k):
        t=Tools()
        size=len(A)
        if size<k:
            A=t.insertionSort(A)
            return A
        else:
            mid=size//2
            left=A[0:mid]
            right=A[mid:]
            #sorting left and right arrays recursively
            left=t.mergeSort(left,k)
            right=t.mergeSort(right,k)
            #merging the left and right sorted arrays into single array mergedA
            mergedA=t.merge(A,left,right)
            return mergedA

    def merge(self, A, left, right):
        mergedA=[]
        for _ in A:
            if len(left)>0 and len(right)>0:
                if left[0]<right[0]:
                    mergedA.append(left[0])
                    left=left[1:]
                else:
                    mergedA.append(right[0])
                    right=right[1:]
        #append the remaining pieces of left or right array to the final merged array
        mergedA=mergedA+left+right
        return mergedA


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

    #Generates a random list of size n
    def genRandom(self,n):
        a=0
        b=n
        A=rd.sample(range(a,b),n)
        return A

    #Returns the time taken to perform merge sort variant
    def mergecompTime(self,A,k):
        t=Tools()
        start=time.clock()
        t.mergeSort(A,k)
        return time.clock() - start

    #Returns the time taken to perform merge sort variant
    def selcompTime(self,A):
        t=Tools()
        start=time.clock()
        t.selectionSort(A)
        return time.clock() - start

if __name__ == "__main__":
	main()