''' Given an unsorted array A of size N that contains only non-negative integers,
find a continuous sub-array which adds to a given number S.
In case of multiple subarrays, return the subarray which comes first
on moving from left to right.'''

def subarray(arr, N, S):
    for i in range(N):
        j=i
        sum=0
        while(sum<S and j<N):
            sum+=arr[j]
            if sum==S:
                return [i+1,j+1]
            j+=1
    return -1

arr=[]
n=int(input('Enter the number of elements in the array'))
print('Enter the array elements')
for i in range(n):
    arr.append(int(input()))
S=int(input('Enter the sum'))
index = subarray(arr, n, S)
print(index)
