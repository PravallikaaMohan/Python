'''Given a vector of N positive integers and an integer X.
The task is to find the frequency of X in vector.'''

def findFrequency(arr,N,num):
    count=0
    for i in range(N):
        if(arr[i]==num):
            count+=1
    return count


arr=[]
N=int(input('Enter the number of elements in the array'))
print('Enter the array elements')
for i in range(N):
    arr.append(int(input()))
num = int(input('Enter the number to find frequency'))
freq=findFrequency(arr,N,num)
if(freq==0):
    print('Number not found')
else:
    print('Frequency of ',num, " is ",freq)
