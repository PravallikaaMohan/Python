'''Given an unsorted array arr[] of size N having both negative and positive integers.
The task is place all negative element at the end of array
without changing the order of positive element and negative element.'''

def segregateElements(arr, N):
    arr1=[]
    for i in range(N):
        if arr[i]<0:
            arr1.append(arr[i])
    for x in arr1:
        arr.remove(x)
    arr=arr1+arr
    print(arr)

arr=[]
N=int(input('Enter the number of elements in the array'))
print('Enter the elements')
for i in range(N):
    arr.append(int(input()))
segregateElements(arr,N)
