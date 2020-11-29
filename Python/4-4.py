def onlyPositives(myTuple:tuple)->tuple:
    """Deletes negative numbers in input tuple and returns new tuple with values in descending order"""
    positivesList = []

    for i in myTuple:
        if i >= 0:
            positivesList.append(i)

    positivesList.sort()
    positivesList.reverse()
    
    return tuple(positivesList)


def main():
    myTuple = (-10, 1, 2, -9, 3, 4, -8, 5, 6)
    print("Original tuple:", myTuple)
    onlyPositiveTuple = onlyPositives(myTuple)
    print("New tuple with positive numbers:", onlyPositiveTuple)


if __name__ == "__main__":
    main()


# Output
##>>> 
##========= RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/Lab4/4-4.py =========
##Original tuple: (-10, 1, 2, -9, 3, 4, -8, 5, 6)
##New tuple with positive numbers: (6, 5, 4, 3, 2, 1)
