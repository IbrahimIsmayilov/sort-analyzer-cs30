# SORT ANALYZER STARTER CODE

import time
import math

# RETURN DATA FROM FILE AS AN ARRAY OF INTERGERS
def loadDataArray(fileName):
    temp = []

    # Read file line by line
    fileref = open(fileName, "r")
    for line in fileref:
        line = line.strip()  # Clean up line
        temp.append(int(line))  # Add integer to temp list

    fileref.close()

    return temp

# LOAD DATA FILE INTO GLOBAL VARIABLES
randomData = loadDataArray("data-files/random-values.txt")
reversedData = loadDataArray("data-files/reversed-values.txt")
nearlySortedData = loadDataArray("data-files/nearly-sorted-values.txt")
fewUniqueData = loadDataArray("data-files/few-unique-values.txt")

# VERIFY LOADED DATA BY PRINTING FIRST 50 ELEMENTS
# print(randomData[0:50])
# print(reversedData[0:50])
# print(nearlySortedData[0:50])
# print(fewUniqueData[0:50])


def bubbleSort(anArray):
    num = len(anArray) - 1
    # Complete the amount of comparisons or passes needed
    for i in range(num):
        # Looping through the array and sorting values
        for n in range(num-i-1):
            # Swap the values if they are out of order
            if anArray[n] > anArray[n+1]:
                anArray[n], anArray[n+1] = anArray[n+1], anArray[n]


def selectionSort(anArray):
    for i in range(len(anArray) - 1):
        # Search for minimum
        minPosition = i
        for n in range(i + 1, len(anArray)):
            if (anArray[n] < anArray[minPosition]):
                minPosition = n
        anArray[i], anArray[minPosition] = anArray[minPosition], anArray[i]


def insertionSort(anArray):
    for i in range(1, len(anArray)):
        # Save the insert value
        insertVal = anArray[i]
        # Save the insert position
        insertPos = i
       
        # Modify the insert position and overwrite it if it does not belong
        while insertPos > 0 and insertVal < anArray[insertPos - 1]:
            anArray[insertPos] = anArray[insertPos - 1]
            insertPos -= 1
        # Insert the value in its proper position and overwrite the duplicate if there was any change in the positions
        anArray[insertPos] = insertVal



# EXAMPLE OF HOW TO TIME DURATION OF A SORT ALGORITHM
startTime = time.time()
insertionSort(randomData)
endTime = time.time()
timeDiff = endTime - startTime 
print(f"{timeDiff}")

