'''Given an array of size N containing only 0s, 1s, and 2s;
sort the array in ascending order.'''

def sort012(arr,N):
    zero=one=two=0
    for i in range(N):
        if(arr[i]==0):
            zero+=1
        elif(arr[i]==1):
            one+=1
        else:
            two+=1
    for i in range(zero):
        arr[i]=0
    for i in range(zero,zero+one):
        arr[i]=1
    for i in range(zero+one,N):
        arr[i]=2
    print(arr)

arr=[]
print('Enter the number of elements in the array')
N=int(input())
print('Enter the elements in the array')
for i in range(N):
    arr.append(int(input()))
sort012(arr,N)
