# Alex Grams
# 1163814
# Program to test performing multiple operations on an array of integers
#
# Define constant variables. 
ONE_TEN = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#ONE_TEN = [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
#ONE_TEN = [5, 3, 1]
#ONE_TEN = [1, 1, 1, 1, 2, 2, 3, 4, 10, 12, 12, 5]
#ONE_TEN = [3, 24, 20, 12, 19, 17, 17, 22, 19, 23, 19, 4, 0, 7, 6, 7, 19, 10, 12, 16, 17, 6, 14, 4, 3, 17, 24, 20, 13, 24, 8, 16]

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


# Output
##>>> 1
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW4/HW4_PS1_a_grams.py ====
##The original data for all functions is:  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
##After swapping first and last:  [10, 2, 3, 4, 5, 6, 7, 8, 9, 1]
##After shifting right:  [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]
##After replacing even elements:  [1, 0, 3, 0, 5, 0, 7, 0, 9, 0]
##After replacing with neighbors:  [1, 3, 4, 5, 6, 7, 8, 9, 10, 10]
##After removing the middle element(s):  [1, 2, 3, 4, 7, 8, 9, 10]
##After moving even elements:  [2, 4, 6, 8, 10, 1, 3, 5, 7, 9]
##The second largest value is:  9
##The list is in increasing order:  True
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 2
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW4/HW4_PS1_a_grams.py ====
##The original data for all functions is:  [12, 20, 10, 14, 54, 16, 75, 38, 79, 103]
##After swapping first and last:  [103, 20, 10, 14, 54, 16, 75, 38, 79, 12]
##After shifting right:  [103, 12, 20, 10, 14, 54, 16, 75, 38, 79]
##After replacing even elements:  [0, 0, 0, 0, 0, 0, 75, 0, 79, 103]
##After replacing with neighbors:  [12, 12, 14, 54, 54, 75, 75, 79, 103, 103]
##After removing the middle element(s):  [12, 20, 10, 14, 75, 38, 79, 103]
##After moving even elements:  [12, 20, 10, 14, 54, 16, 38, 75, 79, 103]
##The second largest value is:  79
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 3
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW4/HW4_PS1_a_grams.py ====
##The original data for all functions is:  [5, 3, 1]
##After swapping first and last:  [1, 3, 5]
##After shifting right:  [1, 5, 3]
##After replacing even elements:  [5, 3, 1]
##After replacing with neighbors:  [5, 5, 1]
##After removing the middle element(s):  [5, 1]
##After moving even elements:  [5, 3, 1]
##The second largest value is:  3
##The list is in increasing order:  False
##The list has adjacent duplicates:  False
##The list has duplicates:  False
##>>> 4
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW4/HW4_PS1_a_grams.py ====
##The original data for all functions is:  [1, 1, 1, 1, 2, 2, 3, 4, 10, 12, 12, 5]
##After swapping first and last:  [5, 1, 1, 1, 2, 2, 3, 4, 10, 12, 12, 1]
##After shifting right:  [5, 1, 1, 1, 1, 2, 2, 3, 4, 10, 12, 12]
##After replacing even elements:  [1, 1, 1, 1, 0, 0, 3, 0, 0, 0, 0, 5]
##After replacing with neighbors:  [1, 1, 1, 2, 2, 3, 4, 10, 12, 12, 12, 5]
##After removing the middle element(s):  [1, 1, 1, 1, 2, 4, 10, 12, 12, 5]
##After moving even elements:  [2, 2, 4, 10, 12, 12, 1, 1, 1, 1, 3, 5]
##The second largest value is:  10
##The list is in increasing order:  False
##The list has adjacent duplicates:  True
##The list has duplicates:  True
##>>> 5
##==== RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/HW4/HW4_PS1_a_grams.py ====
##The original data for all functions is:  [3, 24, 20, 12, 19, 17, 17, 22, 19, 23, 19, 4, 0, 7, 6, 7, 19, 10, 12, 16, 17, 6, 14, 4, 3, 17, 24, 20, 13, 24, 8, 16]
##After swapping first and last:  [16, 24, 20, 12, 19, 17, 17, 22, 19, 23, 19, 4, 0, 7, 6, 7, 19, 10, 12, 16, 17, 6, 14, 4, 3, 17, 24, 20, 13, 24, 8, 3]
##After shifting right:  [16, 3, 24, 20, 12, 19, 17, 17, 22, 19, 23, 19, 4, 0, 7, 6, 7, 19, 10, 12, 16, 17, 6, 14, 4, 3, 17, 24, 20, 13, 24, 8]
##After replacing even elements:  [3, 0, 0, 0, 19, 17, 17, 0, 19, 23, 19, 0, 0, 7, 0, 7, 19, 0, 0, 0, 17, 0, 0, 0, 3, 17, 0, 0, 13, 0, 0, 0]
##After replacing with neighbors:  [3, 20, 20, 20, 20, 20, 22, 22, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 23, 24, 24, 24, 24, 24, 24, 16]
##After removing the middle element(s):  [3, 24, 20, 12, 19, 17, 17, 22, 19, 23, 19, 4, 0, 7, 6, 10, 12, 16, 17, 6, 14, 4, 3, 17, 24, 20, 13, 24, 8, 16]
##After moving even elements:  [24, 20, 12, 22, 4, 0, 6, 10, 12, 16, 6, 14, 4, 24, 20, 24, 8, 16, 3, 19, 17, 17, 19, 23, 19, 7, 7, 19, 17, 3, 17, 13]
##The second largest value is:  23
##The list is in increasing order:  False
##The list has adjacent duplicates:  True
##The list has duplicates:  True
