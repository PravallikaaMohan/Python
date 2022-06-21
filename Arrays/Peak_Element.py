''' An element is called a peak element if its value is not smaller than the value of its adjacent elements(if they exists).
Given an array arr[] of size N, Return the index of any one of its peak elements.
Note: The generated output will always be 1 if the index that you return is correct. Otherwise output will be 0. '''

def peakElement(arr, N):
        for i in range(N):
            if N==1:
                return 1
            if i==N-1:
                if arr[i-1]<arr[i]:
                    return i+1
            else:
                if arr[i+1]<arr[i] and arr[i-1]<arr[i]:
                    return i+1
        return 0


print("Enter the number of elements:")
N=int(input())
arr=[]
print("Enter the elements:")
for i in range(N):
    arr.append(int(input()))
flag = peakElement(arr, N)
if(flag):
    print(1)
    print("Peak Element at position ", flag)
else:
    print(0)
