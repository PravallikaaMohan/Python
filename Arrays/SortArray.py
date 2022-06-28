# Given a random set of numbers, Print them in sorted order.

def Sort(arr, N):
    temp=0
    for i in range(int((N+1)/2)):
        if arr[i]>arr[i+1]:  # Asending order. To print in Descending order arr[i]<arr[i+1]
            temp=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=temp
    return arr

arr=[]
N=int(input('Enter the number of elements in the array'))
print("Enter the elements in the array")
for i in range(N):
    arr.append(int(input()))

#Using predefined function
print(sorted(arr)) #to print in ascending order
print(sorted(arr, reverse=True)) #to print in descending order


#Using Userdefined function Sort(arr,N)
sorted_array = Sort(arr,N)
print(sorted_array)
