'''Given an array, rotate the array by one position in clock-wise direction.'''

def rotate(arr,N):
    temp=arr[N-1]
    for i in range(N-1,-1,-1):
        arr[i]=arr[i-1]
    arr[0]= temp
    print(arr)

N=int(input('Enter the size of array'))
print('Enter the elements')
arr=[]
for i in range(N):
    arr.append(int(input()))
rotate(arr,N)
