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
        n = array.shape[0]
        idx = n-1
        b_array = [[] for i in range(n)]
        for i in range (idx):
            b_array[i] = []

        for j in range(1, n):
            b_array[math.floor(n * array[j])].append(array[j])


        for k in range(idx):
            self.insertion_sort(b_array[k])
            
        for idx, i in enumerate(b_array):
            for j in i:
                array[idx] = j
            
        
        

# arr = np.linspace(0, 0.9, 10)
# random.shuffle(arr) 
# print(arr)
# bucketsort = BucketSort()

# bucketsort.sort(arr)

# print(arr)


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

# arr = [['Player 1','23'],
#  ['Player 2','19'],
#  ['Player 3' ,'36'],
#  ['Player 4' ,'25']]

# sort = HeapSort()
# sort.sort(arr)
# n = len(arr) 

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
        
# arr = [['Player 1','23'],
#  ['Player 2','19'],
#  ['Player 3' ,'36'],
#  ['Player 4' ,'25']]
# n = len(arr)
# sort = QuickSort(order = "dec")
# sort.sort(arr)
# print(arr)

 