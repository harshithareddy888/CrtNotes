#SETS Examples-unordered, unindexed collection of elements
#Empty set
A=set()

B={"hi",34,"hello","cse","vgnt","hello"}
print(B,type(B))  #{34, 'hello', 'cse', 'hi', 'vgnt'} <class 'set'>

print(B[1]) #unindexed & elements immutables-ERROR (TypeError: 'set' object is not subscriptable)


#METHODS
#ADD-----> syntax: setname.add()
c={1,2,3,4,56,35,57,27,68,17,50}
c.add(5)
print(c)   #{1, 2, 3, 4, 5}

#remove()
c.remove(2)
print(c)  #{1, 3, 4, 35, 68, 5, 17, 50, 56, 57, 27}

#discard()
c.discard(57)
print(c)  #{1, 3, 4, 35, 68, 5, 17, 50, 56, 27}

#removing and discarding an unexisting value
#c.remove(100)
print(c)  #throws an error 
c.discard(150)
print(c)  #{1, 3, 4, 35, 68, 5, 17, 50, 56, 27}

#pop()
c.pop()
print(c)

#UNION
#setname.union(setname2)
s1={1,2,3,4}
s2={4,5,6,7}
s3=s1.union(s2)    #s3=s1|s2
s1.update(s2)      #works just like union but this saves memory
print(s3)
print(s1)


#INTERSECTION
#setname.intersection(setname2)
s1={1,2,3,4}
s2={4,5,6,7}
s3=s1.intersection(s2)    #s3=s1&s2
print(s3)
#intersection_update
s1.intersection_update(s2)
print(s1)

#DIFFERENCE
x={1,4,7,9}
y={4,5,6,1}
z=x-y
print(z)
x.difference_update(y)
print(z)

#isdisjoint()
print(s1.isdisjoint(s2))

#issubset()
z=x.issubset(y)
print(z)

#issuperset()
z=y.issuperset(x)
print(z)


x={1,2,3}
y={1,4,5}
#symmetric_difference
z=x.symmetric_difference(y)
print(z)
#READING I/P:
s1=set(input().split())  #i/p format= "hi","hello","cse"
s2=set(map(int,input().split()))   #i/p format: 1 2 3 4 5
s3=eval(input())         #i/p format: {"hi",1,2,"hello"}

