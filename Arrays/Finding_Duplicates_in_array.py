'''Given an array of size N-1 such that it only
 contains distinct integers in the range of 1 to N. Find the missing element.'''

from collections import defaultdict

def duplicates(arr, N):
    d=defaultdict(int)
    for i in arr:
        d[i]+=1
    c=[]
    for i, j in defaultdict.iteritems():
        if j>1:
            c.append(i)
    if c is Null:
        return -1
    else:
        return c

N=int(input('Enter the size of array'))
print('Enter the elements')
arr=[]
for i in range(N):
    arr.append(int(input()))
arr1= duplicates(arr,N)
print(arr1)
