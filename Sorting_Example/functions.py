#Functions for sorting exercise

def cmp(a, b):
    return (a > b) - (a < b) 

def mySort(numbers):
    numbers = bubbleSort(numbers)
    return numbers

def bubbleSort(List):
    for i in range (len(List)):
        for j in range((len(List)-1),i,-1):
            if List[j] < List[j-1]:
                temp = 0
                temp = List[j-1]
                List[j-1] = List[j]
                List[j] = temp
#write your code here
#Sort an unordered list from the smallest to the largest using bubble sort algorithm
    return List

