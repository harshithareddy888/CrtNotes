#NOTE= for any collection of data even if the collection is same, the address is different
#eg:
L1=[1,2,3]
L2=[1,2,3]
print(L1 is L2)

L=[34,"vignan",39.09,True,None,3+7k]
print(L)
print(*L)#to print without brackets and no commas
print(*L,sep='-')#can use separator


L[2]=False  #mutable
print(L)
print(L[-1],L[5])  #negative indexing
#empty list
L1=[]
L2=list() #can be give using a constructor 

#listname.append()
L=[90,80]
L2=[1,2,3]
L.append(100)
L.append([11,12]) #appending array of values
print(L)

#len(L)
print(len(L),type(L))

#extend-method: to append one list with another existing list
L.extend(L2)
print(L)
L.extend([1,2,3])
print(L)
print(len(L),type(L))


#slicing -cutting down the part of list we need into another list
#SYNTAX OF SLICING : listname[start:end:count]

List1=[1,2,3,4,5,6,7,8,9]
L1=L[0:2]+L[-3:-1]  #where we mostly use slicing
print(List1[0:6:1])
print(List1[0:6])  #default count is 1
print(List1[:6])   #default start is 0
print(List1[6:])   #default end value is end of list

print(List1[1:6:-1]) #[]-returns an empty block
print(List1[6:1:-1]) #slices in the reverse order
print(List1[:1:-1]) #starts from the end of list
print(List1[::-1])  #reversing a list
print(List1[::1])   #prints the original list


print(List1[-1:-5:1]) #returns [] since the count is 1 counts from -1 and next
print(List1[-5:-1:1]) #returns [5,6,7,8]
print(List1[-5::1])   #returns [5,6,7,8,9] end index not given so default end is end of the list
print(List1[:-1:1])   #returns [1,2,3,4,5,6,7,8] start index is not given so default start is 0

#INSERT
#SYNTAX OF INSERT: listname.insert(index,value)
List2=[1,2,3,4,5]
List2.insert(1,100)
print(List2)

#REMOVE
#SYNTAX OF REMOVE: listname.remove(index or value)
List2.remove(100)
print(List2)
List2.remove(List2[0])
print(List2)

#INDEX
#SYNTAX OF INDEX : listname.index(value)
print("element 3 is present at index=",List2.index(3))

#POP
#SYNTAX OF POP: listname.pop()    -- returns last element
x=List2.pop()
print(x)
print(List2)

#SORT
#SYNTAX OF SORT : listname.sort()
List3=[29,31,97,66,44,80,63,10000]
List3.sort()           #ascending
print(List3)
List3.sort(reverse=True)
print(List3)

#There are two types of copy
#COPY
#SYNTAX OF COPY: listname.copy()
List3=[29,31,97,66,44,80,63,10000,31,31]
l3=List3.copy()
print(l3)

#ASSIGNMENT COPY
L1=[1,2,3,4]
L2=L1 #Assignment copy
L2.append(5)
print(L2,L1)
#changes gets made to both the lists
print(L1 is L2)  #true
L3=L1.copy()
print(L1 is L3)  #false

#COUNT
#SYNTAX OF COUNT: listname.count(value)  - gives us the no of duplicate elements of that certain value
print(List3.count(31))

#CLEAR
#SYNTAX OF CLEAR :listname.clear()   - deletes the elements in it
print(List3.clear())

#DEL 
#SYNTAX OF DEL :del listname[index]
list2=[1,2,3,3,4]
del list2[0]
print(list2)

#DEL
#SYNTAX OF DEL :del listname
del list2
print(list2)

#BASIC OPERATORS
#  *
L=[1,2,3]
print(L*2)

#  +
L2=[1,3,5,67]
L1=L1+L2
print(L1)

#  in


#Printing List (USING 'FOR EACH' LOOP)
#changes made in for each loop are temporary
#if we want the changes we made to store permenantly we must use range function (list updates / modify exisiting list /manipulate the exisiting list)
L=[90,80,50,67,55,56]

for v in L:
    v+=2
    print(v)
print(L)
#USING RANGE FUNCTION
for i in range(0,len(L)):
    L[i]+=2
    print(L[i])
print(L)

#reading I/P :
# for single line i/p's
#I/P:5
    10                  
    26
    30
    50
    23#
n=int(input())
L=[]
for i in range(0,n):
    L.append(int(input()))
print(L)

#for this type of output
'''i/p:5
       10 26 30 50 23 '''
n=int(input())
L=list(map(int,input().split()))
print(L)


#i/p:[3,4,5,6,7,8]
L=eval(input())   #eval is function which evaluates the input and assigns it to list/tuple
print(L,type(L))



#NESTED LIST
#Its just like matrices/arrays

L=[[1,2],[6,7],[8,9]]
print(L[2])
print(L[2][1])  #9

for v in L:     #printing rows
    print(v)
    
for v in L:     #printing each element in v
    for e in v:
        print(e)


for i in range(0,3):
    for j in range(0,2):   #accessing and modifying elements
        #L[i][j]=L[i][j]+5 
        print(L[i][j])

#WHENEVER WE DON'T HAVE "range" IN "for loop" WE CAN'T MANIPULATE OR MODIFY THE DATA


#SUM OF MATRIX
L=[[1,2,3],[6,7,8],[11,12,13]]
for i in range(0,3):
    for j in range(0,3):
    # ???




#Reading matrix
     #i/p:3
             #1 9 8
             #6 7 4
             #3 2 5
             
n=int(input())
matrix=[]
for i in range(0,n):
    row=list(map(int,input().split()))
    matrix.append(row)
print(matrix)


#Reading matrix
#i/p:[[1,2,3],[4,5,6],[7,8,9]]

n=int(input())
matrix=eval(input())
for i in range(0,n):
    row=list(map(int,input().split()))
    matrix.append(row)
print(matrix)



