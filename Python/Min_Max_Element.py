def getMinMax(arr, N):
    min=max=0
    for i in range(N):
        if(arr[i]<min):
            min=arr[i]
        elif(arr[i]>max):
            max=arr[i]
    return min, max


print("Enter the number of elements in an array")
N=int(input())
print("Enter the elements")
arr=[]
for i in range(N):
    arr.append(int(input()))
Min, Max = getMinMax(arr,N)
print("Minimum: ",Min)
print("Maximum: ",Max)
