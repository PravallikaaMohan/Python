'''Given an array of size N-1 such that it only contains distinct integers
 in the range of 1 to N. Find the missing element.'''

def MissingNumber(arr, N):
    if N not in arr:
        return N
    else:
        for i in range(1,N):
            if i in arr:
                continue
            else:
                return i

N=int(input('Enter the size of array'))
arr=[]
for i in range(N-1):
    arr.append(int(input()))
num = MissingNumber(arr,N)
print('Missing Number:',num)
