def biggie_size(arr):
    for i in range(0,len(arr)):
        if arr[i]>0:
            arr[i] = 'big'
    return arr
print(biggie_size([-1,3,5,-5]))

def count_positives(arr):
    count = 0
    for i in range(0,len(arr)):
        if(arr[i]>0):
            count +=1
    arr[len(arr)-1] = count
    return arr
print(count_positives([-1,1,1,1]))
print(count_positives([1,6,-4,-2,-7,-2]))

def sum_total(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    return sum
print(sum_total([1,2,3,4]))
print(sum_total([6,3,-2]))

def average(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum += arr[i]
    avg = sum/len(arr)
    return avg
print(average([1,2,3,4]))

def length(arr):
    x = len(arr)
    return x
print(length([37,21,1,-9]))
print(length([]))

def minimum(arr):
    if(len(arr)==0):
            return False
    min = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]<min):
            min = arr[i]
    return min
print(minimum([37,2,1,-9]))
print(minimum([]))

def maximum(arr):
    if(len(arr)==0):
            return False
    max = arr[0]
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max = arr[i]
    return max
print(maximum([37,2,1,-9]))
print(maximum([]))

def ultimate_analysis(arr):
    x = {}
    min = arr[0]
    max = arr[0]
    sumTotal = arr[0]
    length = len(arr)
    for i in range(1,len(arr)):
        if(arr[i]>max):
            max = arr[i]
        elif(arr[i]<min):
            min = arr[i]
        sumTotal += arr[i]
        avg = sumTotal/len(arr)
    results = {'sumTotal': sumTotal,'average': avg, 'minimum': min, 'maximum': max, 'length':length}
    return results
print(ultimate_analysis([37,2,1,-9]))

def reverse_list(arr):
    for i in range(0,len(arr)):
        if(i > len(arr)-1-i):
            return arr
        else:
            temp = arr[i]
            arr[i]= arr[len(arr)-1-i]
            arr[len(arr)-1-i] = temp
    # return list(reversed(arr)) 
    # quick non for loop solution    
print(reverse_list([37,2,1,-9]))