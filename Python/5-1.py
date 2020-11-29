# Question 1
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
    
    print("Key/value pairs: ", end = "")
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


# Output:
##>>> 
##========= RESTART: C:/Users/Alex/Documents/IVC/CS 10 HW/Lab5/5-1.py =========
##Keys: A D B F C 
##Values: 8 3 15 2 6 
##Key/value pairs: A:8 D:3 B:15 F:2 C:6 
##Key/value pairs sorted by key: A:8 B:15 C:6 D:3 F:2 
##Average value: 6.8
