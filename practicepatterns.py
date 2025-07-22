#a
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or j==n or i==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#e
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or j==1 or i==n or i==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
#i
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==(n//2)+1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
#o
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==1 or i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

#u
n=int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==n or j==1 or j==n:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
