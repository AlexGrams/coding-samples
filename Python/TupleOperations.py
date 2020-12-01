# Author: Alex Grams
#
# Tests performing multiple operations on an array of integers

# Define constant variables. 
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def swapFirstLast(data:list)->None:
    """Swaps first and last elements of input list"""
    temp = data[0]

    data[0] = data[len(data) - 1]
    data[len(data) - 1] = temp


def shiftRight(data:list)->None:
    """Shifts elements in list one place to the right and moves last element to front"""
    data.insert(0, data[len(data) - 1])
    del data[len(data) - 1]


def replaceEven(data:list)->None:
    """Replaces all even elements in input list with 0"""
    for i in range(len(data)):
        if data[i] % 2 == 0:
            data[i] = 0


def replaceNeighbors(data:list)->None:
    """Replaces each element in list with larger of two neighbors"""
    for i in range(1, len(data) - 1):
        if data[i + 1] > data[i - 1]:
            data[i] = data[i + 1]
        else:
            data[i] = data[i - 1]


def removeMiddle(data:list)->None:
    """Removes middle element(s) of list"""
    if len(data) % 2 == 0:
        del data[len(data) // 2]
    del data[len(data) // 2]


def evenToFront(data:list)->None:
    """Moves all even numbers of the list to the front while maintaining their original order"""
    i = len(data) - 1
    end = 0

    while i >= end:
        if data[i] % 2 == 0:
            temp = data[i]

            del data[i]
            data.insert(0, temp)
            end += 1
        else:
            i -= 1


def secondLargest(data:list)->int:
    """Finds and returns second largest value in the list"""
    if data[0] > data[1]:
        largest = data[0]
        secondLargest = data[1]
    else:
        largest = data[1]
        secondLargest = data[0]

    for i in range(2, len(data)):
        if data[i] > largest:
            secondLargest = largest
            largest = data[i]
        elif data[i] > secondLargest and data[i] != largest:
            secondLargest = data[i]

    return secondLargest


def isIncreasing(data:list)->bool:
    """Determines if the list is currently in increasing order"""
    for i in range(1, len(data)):
        if data[i] < data[i - 1]:
            return False

    return True


def hasAdjacentDuplicate(data:list)->bool:
    """Returns true if list has adjacent duplicate elements"""
    for i in range(1, len(data) - 1):
        if data[i] == data[i + 1]:
            return True

    return False


def hasDuplicate(data:list)->bool:
    """Returns true if list contains duplicate elements"""
    for i in range(0, len(data) - 1):
        if data[i] in data[i + 1:]:
            return True

    return False
    

def main() : 
    print("The original data for all functions is: ", ONE_TEN) 
    #   a.   Demonstrate swapping the first and last element. 
    data = list(ONE_TEN) 
    swapFirstLast(data) 
    print("After swapping first and last: ", data) 
    #   b.   Demonstrate shifting to the right. 
    data = list(ONE_TEN) 
    shiftRight(data) 
    print("After shifting right: ", data) 
    #   c.   Demonstrate replacing even elements with zero. 
    data = list(ONE_TEN) 
    replaceEven(data) 
    print("After replacing even elements: ", data) 
    #   d.   Demonstrate replacing values with the larger of their neighbors. 
    data = list(ONE_TEN) 
    replaceNeighbors(data) 
    print("After replacing with neighbors: ", data) 
    #   e.   Demonstrate removing the middle element. 
    data = list(ONE_TEN) 
    removeMiddle(data) 
    print("After removing the middle element(s): ", data) 
    #   f.   Demonstrate moving even elements to the front of the list. 
    data = list(ONE_TEN) 
    evenToFront(data) 
    print("After moving even elements: ", data) 
    #   g.   Demonstrate finding the second largest value. 
    print("The second largest value is: ", secondLargest(ONE_TEN)) 
    #   h.   Demonstrate testing if the list is in increasing order. 
    print("The list is in increasing order: ", isIncreasing(ONE_TEN)) 
    #   i.   Demonstrate testing if the list contains adjacent duplicates. 
    print("The list has adjacent duplicates: ", hasAdjacentDuplicate(ONE_TEN)) 
    #   j.   Demonstrate testing if the list contains duplicates. 
    print("The list has duplicates: ", hasDuplicate(ONE_TEN))


if __name__ == "__main__":
    main()
    