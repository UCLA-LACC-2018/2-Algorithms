#Functions for sorting exercise

def cmp(a, b):
    return (a > b) - (a < b)

def mySort(numbers):
    numbers = bubbleSort(numbers)
    return numbers

def bubbleSort(List):
#write your code here
#Sort an unordered list from the smallest to the largest using bubble sort algorithm
    for i in reversed(range(len(List))):
        for j in range(i):
            if List[j] > List[j+1]:
                temp = List[j]
                List[j] = List[j+1]
                List[j+1] = temp
    return List
