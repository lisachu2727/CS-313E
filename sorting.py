#File: sorting.py
#Descriptiong: HW 9
#Student's Name: Lisa Chu
#Student's UT EID: tc29328
#Course Name: CS 313E
#Unique Number: 50739
#
#Date Created: 4/25/19
#Date Last Modified: 4/26/19

#############################################################################
#Start of given code

import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1


def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark
#End of given code
#############################################################################

#All the sorting using bubble sort
def bubbleTrials():
    #List to store all the average times
    bubble = []

    #Sorting random lists of sizes 10, 100, 1000
    #then computing average run times and appending to list
    
    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime
        
    average = format(average/5, '.6f')      
    bubble.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    #Sorting sorted lists of sizes 10, 100, 100
    #then appending average run time to list
    
    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    #Sorting reversed lists of sizes 10, 100, 1000
    #then computing average run time and appending to list
    
    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    #Sorting almost sorted lists of sizes 10, 100, 100
    #then computing average run time and appending to list
    
    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        bubbleSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    bubble.append(average)

    #returning list of averages
    
    return bubble

#Sorting using insertion sort

def insertionTrials():
    #List to store average sort times
    insertion = []
    
    #Sorting random lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    #Sorting sorted lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    #Sorting reverse lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    #Sorting almost sorted lists of sizes 10, 100, 1000
    #then computing average run time and appending to list
    
    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        insertionSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    insertion.append(average)

    #returns list of averages
    
    return insertion

#Sorting using merge sort

def mergeTrials():
    #Creating list to store average run times
    merge = []

    #Sorting random lists of size 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    #Sorting sorted lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    #Sorting reverse lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    #Sorting almost sorted lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        mergeSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    merge.append(average)

    #returns list of averages
    
    return merge

#Sorting using quick sort

def quickTrials():
    #List to store average run times
    quick = []

    #Sorting random lists of size 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        random.shuffle(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    #Sorting sorted lists of size 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    #Sorting reversed lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList.reverse()
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    #Sorting almost sorted lists of sizes 10, 100, 1000
    #then computing average run time and appending to list

    n = 10
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 100
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    n = 1000
    average = 0
    for i in range(5):
        myList = [i for i in range(n)]
        myList = almostSortedList(myList)
        startTime = time.perf_counter()
        quickSort(myList)
        endTime = time.perf_counter()
        elapsedTime = endTime - startTime
        average += elapsedTime

    average = format(average/5, '.6f')
    quick.append(average)

    return quick

def almostSortedList(myList):
    n = len(myList)
    for i in range(n // 10):
        num1 = random.randint(0, n - 1)
        num2 = random.randint(0, n - 1)
        temp = myList[num1]
        temp2 = myList[num2]
        myList[num1] = temp2
        myList[num2] = temp

    #returns list of averages
    return myList

#Prints out all the sorting averages for each method and list type  
def printResults():
    #Retrieving results of all sorting methods
    bubble = bubbleTrials()
    insertion = insertionTrials()
    merge = mergeTrials()
    quick = quickTrials()

    #Printing out results in table form
    
    print('Input type = Random')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort ', bubble[0], bubble[1], bubble[2],sep = '   ')
    print('   insertionSort ', insertion[0], insertion[1], insertion [2], sep = '   ')
    print('       mergeSort ', merge[0], merge[1], merge[2], sep = '   ')
    print('       quickSort ', quick[0], quick[1], quick[2], sep = '   ')
    print()
    print()
    print('Input type = Sorted')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort ', bubble[3], bubble[4], bubble[5],sep = '   ')
    print('   insertionSort ', insertion[3], insertion[4], insertion [5], sep = '   ')
    print('       mergeSort ', merge[3], merge[4], merge[5], sep = '   ')
    print('       quickSort ', quick[3], quick[4], quick[5], sep = '   ')
    print()
    print()    
    print('Input type = Reverse')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort ', bubble[6], bubble[7], bubble[8],sep = '   ')
    print('   insertionSort ', insertion[6], insertion[7], insertion [8], sep = '   ')
    print('       mergeSort ', merge[6], merge[7], merge[8], sep = '   ')
    print('       quickSort ', quick[6], quick[7], quick[8], sep = '   ')
    print()
    print()
    print('Input type = Almost sorted')
    print('                    avg time   avg time   avg time')
    print('   Sort function     (n=10)    (n=100)    (n=1000)')
    print('-----------------------------------------------------')
    print('      bubbleSort ', bubble[9], bubble[10], bubble[11],sep = '   ')
    print('   insertionSort ', insertion[9], insertion[10], insertion [11], sep = '   ')
    print('       mergeSort ', merge[9], merge[10], merge[11], sep = '   ')
    print('       quickSort ', quick[9], quick[10], quick[11], sep = '   ')
    print()
    print()

def main():
    printResults()
    
main()
