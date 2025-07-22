
#tuple is also a collection data which is immutable(values cannot be changed)
#CREATION OF TUPLE
a1=()#empty
a2=tuple()#empty tuple using a constructor
print(a1,a2)

T=(1,2,3,"hi",9.1,True)
print(T, type(T))
print(*T)
print(T[2])

#Tuple must have more than 1 element in it (even if it has one element we should use a , next to it to make it identify as a tuple)
T2=(1,) #one value in tuple
print(T2)
T2.append(3)

#excersice- applying list methods on a tuple
#append
T=(1,78,2,30,22,11,56)
print("appending method")
T.append(100)
print(T)
#o/p:  AttributeError: 'tuple' object has no attribute 'append'


#extend
T=(1,78,2,30,22,11,56)
T2=(10,7,8)
T.extend(T2)
print(T)
#o/p:  AttributeError: 'tuple' object has no attribute 'extend'


#slicing
T=(1,78,2,30,22,11,56)
print(T[0:3:1])
#o/p:(1, 78, 2)

#Insert
T=(1,78,2,30,22,11,56)
T.insert(1,100)
print(T)
#o/p:  AttributeError: 'tuple' object has no attribute 'insert'

#remove
T=(1,78,2,30,22,11,56)
T.remove(100)
print(T)
#O/P:  AttributeError: 'tuple' object has no attribute 'remove'

#index
T=(1,78,2,30,22,11,56)
print("element 78 is present at",T.index(78))
#O/P: element 78 is present at 1

#POP
T=(1,78,2,30,22,11,56)
x=T.pop()
print(x)
#O/p:  AttributeError: 'tuple' object has no attribute 'pop'


#sort
T=(1,78,2,30,22,11,56)
T.sort()
print(T)
#O/P:  AttributeError: 'tuple' object has no attribute 'sort'
#.....

t1=(1,2,3,4,5,6)
t2=(1,2,3,4,5,6)
print(id(t1),id(t2)) #same address

#changes are stored in different addresses (proves the immutable concept)
#using * operator
t1=t1*2
print(id(t1))  #stored in diff address which proves that t1 is not getting updated/modified

#using + operator
t1=t1[0:2]+t1[4:]
print(id(t1))  #stored in diff address which proves that t1 is not getting updated/modified

#Printing TUPLE USING for each
for i in t1:
    print(i)
#above output will be
   
        #1
        #2
        #5
        #6

#printing tuple using for
for i in range(0,len(t1)):
    print(t1[i])
#both of the above output will be
        #1
        #2
        #3
        #4
        #5
         


#READING TUPLE
#i/p: 3 4 7 8 9
t=tuple(map(int,input().split()))
print(t)

#i/p:(1,2,3,4)
t=eval(input())
print(t)

#i/p: 3 hi 89.77 None
t=tuple(input().split())
print(t)

#i/p:4
    #45
    #50
    #55
    #60
n=int(input())
t=list()
for i in range(n):
        v=int(input())
        t.append(v)
print(t,type(t))
t=tuple(t)
print(t,type(t))
    


