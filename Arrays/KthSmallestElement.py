'''Given an array arr[] and an integer K where K is smaller than size of array,
the task is to find the Kth smallest element in the given array.
It is given that all array elements are distinct.'''

def kthSmallest(arr,N,k):
    Sort = sorted(arr)
    print(Sort[k-1])


arr=[]
N=int(input('Enter the elements in the array'))
print('Enter the elements in the array')
for i in range(N):
    arr.append(int(input()))
k=int(input('Enter the index k'))
kthSmallest(arr,N,k)
