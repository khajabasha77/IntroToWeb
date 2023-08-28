# 4. Write a function to remove duplicates from a sorted array. Use any language of your choice.

# list_a = [1,1,2,3,4,4,4,5,5,6,7,7]

def remove_duplicates(list_a):
    unique_list = []
    for i in range(len(list_a)):
        if (list_a[i] not in unique_list):
            unique_list.append(list_a[i])
    return unique_list
    
list_a = list(map(int, input().split(",")))
result = remove_duplicates(list_a)
print(result)
#print(list(set(list_a)))

#---------------------------------------------------------------------------->

#5. Write the following function, that splits passed arr into two arrays, the first containing values smaller than the value and the second array containing values larger than the value.
def split_array(arr):
    if(n%2==0):
        print(arr[:a/2], arr[a/2:])
    else:
        print(arr[:a-1], arr[a-1:])

arr = list(map(int, input().split(","))) #8,6,7,5,2,3,1,4,9
n = len(arr)
a = int(n/2)
arr = sorted(arr)
split_array(arr)
#------------------------------------------------------------------------------>

#6. Write a function mergeSorted which merges two sorted arrays into a sorted array with the time complexity of O(n) and space complexity of O(n).

def merged_sorted(list_a, list_b):
    list_a, list_b = sorted(list_a), sorted(list_b)
    return sorted(list_a+list_b)
list_a = list(map(int, input().split(","))) # 2,3,1,4
list_b = list(map(int, input().split(","))) # 8,9,6,7,5
print(merged_sorted(list_a,list_b)) #1,2,3,4,5,6,7,8,9
