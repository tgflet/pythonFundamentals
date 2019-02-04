def countdown(x):
    arr =[]
    for i in range(x,-1,-1):
        arr.append(i)
    return arr
print(countdown(5))

def print_and_return(x):
    print(x[0])
    return x[1]
print(print_and_return([1,2]))

def first_plus_length(x):
    sum = x[0]+len(x)
    return sum
print(first_plus_length([1,2,3,4,5]))

def values_greater_than_second(x):
    newArr = []
    counter = 0
    for i in range(0,len(x)):
        if len(x) < 2:
            return False
        elif x[i]>x[1]:
            newArr.append(x[i])
            counter += 1
    print(counter)
    return newArr
print(values_greater_than_second([5,2,3,2,1,4]))
print(values_greater_than_second([3]))

def length_and_values(a,b):
    arr=[]
    for i in range(0,a):
        arr.append(b)
    return arr
print(length_and_values(4,7))
print(length_and_values(6,2))