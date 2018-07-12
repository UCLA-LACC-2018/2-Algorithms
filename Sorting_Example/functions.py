#Functions for sorting exercise

def cmp(a, b):
    return (a > b) - (a < b) 

def mySort(numbers):
    numbers = bubbleSort(numbers)
    return numbers

def bubbleSort(List):
    for x in range (len(List) - 1):
        for y in range (len(List) - x - 1):
            if List[y] > List[y + 1]:
                yeet = List[y]
                List[y] = List[y + 1]
                List[y + 1] = yeet
#write your code here
#Sort an unordered list from the smallest to the largest using bubble sort algorithm
    return List