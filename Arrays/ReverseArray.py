#Given an array A of size N, print the reverse of it.

print('Enter the number of test cases:')
T=int(input())
for i in range(T):
    print('Enter the number of elements in the array')
    N=int(input())
    arr=[]
    print('Enter the elements in the array')
    for i in range(N):
        arr.append(int(input()))
    rev = arr[::-1]  #Using slicing. You can also use reverse() to reverse an array.
    print(rev)
