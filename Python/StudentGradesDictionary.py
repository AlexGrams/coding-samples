# Author: Alex Grams
# Performs operations such as printing key-value pairs and finding the average
# of a dictionary containing letter grades of students in a classroom.

def main():
    grade = {"A":8, "D":3, "B":15, "F":2, "C":6}

    print("Keys: ", end = "")
    for key in grade:
        print(key, end = " ")
    print()
    
    print("Values: ", end = "")
    for value in grade.values():
        print(value, end = " ")
    print()
    
    print("Key-value pairs: ", end = "")
    for key in grade:
        print(key + ":" + str(grade[key]), end = " ")
    print()
    
    keys = list(grade.keys())
    keys.sort()
    print("Key/value pairs sorted by key: ", end = "")
    for key in keys:
        print(key + ":" + str(grade[key]), end = " ")
    print()

    total = 0
    for value in grade.values():
        total += value
    print("Average value: " + str(total/len(grade)))
    
    
if __name__ == "__main__":
    main()
