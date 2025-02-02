# 4/5 --> 1,2,3,5
#1. Write a Python program to sort a list of tuples by the second element.
def sort_by_second_element(list):
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if list[j][1] > list[j + 1][1]:  
                list[j], list[j + 1] = list[j + 1], list[j] 
    return list

list = [(1, 3), (4, 1), (2, 5), (3, 2)]
sorted_list = sort_by_second_element(list)
print(sorted_list)

#2. Develop a program to find the second largest element in a list.
def second_largest(lst):
    if len(lst) < 2:
        return None 
    if lst[0] > lst[1]:
        largest, second = lst[0], lst[1]
    else:
        largest, second = lst[1], lst[0]
    for i in range(2, len(lst)):
        if lst[i] > largest:
            second = largest
            largest = lst[i]
        elif lst[i] > second and lst[i] != largest:
            second = lst[i]
    return second if largest != second else None  
numbers = [10, 20, 4, 45, 99, 99, 45]
print(second_largest(numbers)) 

#3. Create a function to count the frequency of elements in a list.
def count_frequency(lst):
    frequency = {}  
    for item in lst:
        if item in frequency:
            frequency[item] += 1
        else:
            frequency[item] = 1   
    return frequency
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(count_frequency(numbers))

#5. Implement a program to find the most common element in a list.
def most_common_element(lst):
    if not lst:
        return None 
    frequency = {}  
    max_count = 0
    most_common = 0
    for item in lst:
        if item in frequency:
            frequency[item] += 1  
        else:
            frequency[item] = 1  
        if frequency[item] > max_count:
            max_count = frequency[item]
            most_common = item
    return most_common
numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(most_common_element(numbers))  

