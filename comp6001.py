import numpy as np
import time
import random

# Selection Sort
def selection_sort(arr):
    ''' Find the smallest number in the array '''
    start_time = time.time()
    for i in range(len(arr)):
        minimum = arr[i]
        for j in range(i+1, len(arr)):
            if arr[j] < minimum:
                minimum = arr[j]
                arr[j] = arr[i]
                arr[i] = minimum
    #print(arr)
    #print(f"%.4f" %(time.time() - start_time))
    return time.time() - start_time


# Bubble Sort
def bubble_sort(arr):
    ''' Compare with the previous number in the array '''
    start_time = time.time()
    for i in range(len(arr)):
        for j in range(1, len(arr)-i):
            if arr[j] < arr[j-1]:
                temp = arr[j]
                arr[j] = arr[j-1]
                arr[j-1] = temp
    #print(arr)
    #print(f"%.4f" %(time.time() - start_time))
    return time.time() - start_time

# Insertion Sort
def insertion_sort(arr):
    ''' Find the biggest number in the array '''
    start_time = time.time()
    for i in range(len(arr)):
        maximum_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[maximum_index]:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                maximum_index = j
    #print(arr)
    #print(f"%.4f" %(time.time() - start_time))
    return time.time() - start_time


# MergeSort
def split_arrays(arr):
    if len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] <= arr[1] else [arr[1], arr[0]]
    elif len(arr) == 1:
        return [arr[0]]
    else:
        left = split_arrays(arr[:(len(arr)//2)])
        right = split_arrays(arr[(len(arr)//2):])
        #print(left, right)
        return merge_arrays(left, right)

def merge_arrays(left, right):
    left_index, right_index, max_left, max_right = 0, 0, len(left), len(right)
    res = []
    #for(i=0; i < max_left + max_right; i++):
    for i in range(0, max_left + max_right):
        #print(left_index, right_index, max_left, max_right)
        if left_index == max_left:
            res += right[right_index:]
            break
        elif right_index == max_right:
            res += left[left_index:]
            break
        elif left[left_index] > right[right_index]:
            res.append(right[right_index])
            right_index+=1
        else:
            res.append(left[left_index])
            left_index+=1
    #print(res)
    return res

def merge_sort(arr):
    ''' Dividing the input array into smaller subarrays and sorting those subarrays then merging them back together to obtain the sorted array '''
    start_time = time.time()
    split_arrays(arr)
    #print(f"%.4f" %(time.time() - start_time))
    return time.time() - start_time

# QuickSort
def split_arrays(arr):
    if len(arr) == 2:
        return [arr[0], arr[1]] if arr[0] <= arr[1] else [arr[1], arr[0]]
    elif len(arr) == 1:
        return [arr[0]]
    else:
        random_int = random.randint(0, len(arr)-1)
        #print(random_int)
        try:
            left = split_arrays(arr[:random_int])
        except:
            left = split_arrays([arr[random_int]])
            random_int += 1
        try:
            right = split_arrays(arr[random_int:])
        except:
            right = split_arrays([arr[random_int]])
        #print(left, right)
        return merge_arrays(left, right)


def merge_arrays(left, right):
    left_index, right_index, max_left, max_right = 0, 0, len(left), len(right)
    res = []
    #for(i=0; i < max_left + max_right; i++):
    for i in range(0, max_left + max_right):
        #print(left_index, right_index, max_left, max_right)
        if left_index == max_left:
            res += right[right_index:]
            break
        elif right_index == max_right:
            res += left[left_index:]
            break
        elif left[left_index] > right[right_index]:
            res.append(right[right_index])
            right_index+=1
        else:
            res.append(left[left_index])
            left_index+=1
    #print(res)
    return res


def quick_sort(arr):
    ''' Take an array of values, choose one of the values as the 'pivot' element, and move the other values so that lower values are on the left of the pivot element, and higher values are on the right of it. '''
    start_time = time.time()
    split_arrays(arr)
    #print(f"%.4f" %(time.time() - start_time))
    return time.time() - start_time


#main function
if __name__ == "__main__":
    arr1 = list(np.random.randint(low=1, high=1000, size=100))
    arr2 = list(np.random.randint(low=1, high=1000, size=1000))
    arr3 = list(np.random.randint(low=1, high=1000, size=10000))
    print("Algorithm \t\t|\t\tN=100\t\t|\t\tN=1000\t\t|\t\tN=10000")
    print(f"Selection {selection_sort(arr1):>22.10f} {selection_sort(arr2):>20.10f} {selection_sort(arr3):>20.10f}" )
    print(f"Bubble    {bubble_sort(arr1):>22.10f} {bubble_sort(arr2):>20.10f} {bubble_sort(arr3):>20.10f}" )
    print(f"Insertion {insertion_sort(arr1):>22.10f} {insertion_sort(arr2):>20.10f} {insertion_sort(arr3):>20.10f}" )
    print(f"Merge     {merge_sort(arr1):>22.10f} {merge_sort(arr2):>20.10f} {merge_sort(arr3):>20.10f}" )
    print(f"Quick     {quick_sort(arr1):>22.10f} {quick_sort(arr2):>20.10f} {quick_sort(arr3):>20.10f}" )


