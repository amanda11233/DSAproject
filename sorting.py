import numpy as np
import random
import math

class BucketSort():
    def __init__(self):
        pass
    def insertion_sort(self, array):
        n = len(array)
        for j in range(1, n):
            key = array[j]
            i = j -1
            while (i >= 0 and array[i] > key):
                array[i + 1] = array[i]
                i = i - 1
            array[i + 1] = key 
    def sort(self, array):
        n = len(array)
        idx = n-1
        b_array = [[] for i in range(n)]
        for i in range (idx):
            b_array[i] = []

        for j in range(1, n):
            b_array[math.floor(n * (int(array[j][1]) / 100))].append(array[j])


        for k in range(idx):
            self.insertion_sort(b_array[k])
            
        for idx, i in enumerate(b_array):
            for j in i:
                array[idx] = j
 

class HeapSort():
    def __init__(self):
        pass
    def heapify(self, arr, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and arr[i][1] < arr[l][1]:
            largest = l
        if r < n and arr[largest][1] < arr[r][1]:
            largest = r
        if largest != i:
            arr[i],arr[largest] = arr[largest],arr[i]
            self.heapify(arr, n, largest)

    def sort(self, arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(arr, n, i)
        for i in range(n-1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
 
class QuickSort():
    def __init__(self, order = "asc"): 
        self.order = order

    def partition(self, arr, low, high):
        i = (low-1) 
        pivot = int(arr[high][1])
        for j in range(low, high): 
            if(self.order == "asc"):
                if int(arr[j][1]) <= pivot:
                    i = i+1 
                    arr[i], arr[j] = arr[j], arr[i]
            elif(self.order == "dec"):
                if int(arr[j][1]) >= pivot:
                    i = i+1
                    arr[i], arr[j] = arr[j], arr[i]

        arr[i+1], arr[high] = arr[high], arr[i+1]
        return (i+1)

    def sort(self, arr, low=None, high=None): 
        if low == None:
            low = 0
        if high == None:
            high = len(arr) - 1 

        if len(arr) == 1:
            return arr
        if low < high:
            pi = self.partition(arr, low, high)
            self.sort(arr, low, high = pi-1)
            self.sort(arr, low = pi+1, high = high)
        
 

class CountingSort():
     def __init__(self):
         pass
     def sort(self, array, max__):
        k = max__
        n = len(array)
        c_array = [0 for _ in range(k+1)]
        b_array = [[_[0], 0] for _ in array]
        for i in range(k):
            c_array[i] = 0
        for j in range(n):
            c_array[int(array[j][1])] = c_array[int(array[j][1])] + 1
        for i in range(1, k+1):
            c_array[i] = c_array[i] + c_array[i - 1]
        for j in reversed(range(n)):
            b_array[c_array[int(array[j][1])]-1][0] = array[j][0]
            b_array[c_array[int(array[j][1])]-1][1] = int(array[j][1])
            c_array[int(array[j][1])] = c_array[int(array[j][1])] - 1
        return b_array
 