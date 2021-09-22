def countdown(num):
    arr = []
    for x in range (num,-1,-1):
        if num > 0:
            arr.append(x)
    return arr
print(countdown(5))

def print_and_return(num1,num2):
    print(num1)
    print(num2)
print_and_return(1,2)

def first_plus_length(arr):
    x = arr[0] + len(arr)
    return x
arr = [1,2,3,4,5]
print(first_plus_length(arr))

def values_greater_than_second (list):
    if len(list) < 2: 
            return "false" 
    sum = 0
    new_array = []
    for x in range(len(list)):
        if list[x] > list[1]:
            sum+=1
            new_array.append(list[x])
    print(sum)
    return new_array
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def this_length_that_value (num1,num2):
    arr = []
    for i in range(num1):
        arr.append(num2)
    return arr
print(this_length_that_value(4,7))
print(this_length_that_value(6,2))


