# Method 1; utilizing value of elements
def sum_elements_value(arr):
    total= 0
    for element in arr:
        total += element
    return total

#Method 2: Using index of elements
def sum_elements_index(arr):
    total= 0
    for i in range(len(arr)):
        total += arr[i]
    return total

#Example used
arr = [1, 2, 3, 4, 5]
print("Sum of elements utilizing value:", sum_elements_value(arr))
print("Sum of elements utilizing index:", sum_elements_index(arr)) 


