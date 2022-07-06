'''Given two arrays a[] and b[] of size n and m respectively.
 The task is to find union between these two arrays.'''

def doUnion(a,n,b,m):
     c=[]
     for i in range(n):
         if a[i] not in c:
             c.append(a[i])
     for j in range(m):
         if b[j] not in c:
            c.append(b[j])
     return c

n,m=map(int,input('Enter the number of elements in both the arrays').split())
print('Enter the elements in both the arrays')
a=[]
b=[]
for i in range(int(n)):
    a.append(int(input()))
for j in range(int(m)):
    b.append(int(input()))
arr=doUnion(a,int(n),b,int(m))
print(arr)
