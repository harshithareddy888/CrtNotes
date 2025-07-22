# DAY1- 1 ques- without using sliding window
"""k=int(input())
l=list(map(int,input().split(',')))
le=len(l)
for i in range(0,le-k+1):
    s=0
    m=0
    for j in range(i,i+k):
        s+=l[j]
    m=max(m,s)
    print(m)
"""

#DAY1- 2 ques- with using sliding window
"""
k=int(input())
l=list(map(int,input().split(',')))
li=[]
s=0
m=0
for i in range(0,k):
    s+=l[i]
m=s
for j in range(k,len(l)):
    s+=l[j]
    s-=l[j-k]
    m=max(m,s)
print(s)"""


#DAY1- 3 ques- max and min values of subwindow"""
"""
k=int(input())
l=list(map(int,input().split(',')))
li=[]
s=0
m=0
for i in range(0,k):
    #s+=l[i]
    li.append(l[i])
print(max(li))
for j in range(k,len(l)):
    li.append(l[j])
    li.pop(0)
    print(max(li))
"""


#4th ques- unique elements of every window"""
"""
k=int(input())
a=list(map(int,input().split(',')))
d={}
for i in range(k):
    if a[i] in d:
        d[a[i]]+=1
    else:
        d[a[i]]=1
for i in d:
    print(i,end=' ')
for j in range(k,len(a)):
    if a[j] in d:
        d[a[j]]+=1
    else:
        d[a[j]]=1
    if d[a[j]]>1:
          d[a[j]]-=1
    else:
        pop(a[j-k])
print(j, end=' ')

""" 
#DAY2- 5th ques- find the subarray whos sum is equal to the given value (error code? using for)
"""
final_sum=int(input())
a=list(map(int,input().split()))
s=0
for i in range(0, len(a)):
    s+=a[i]
    #print(s)
    for j in range(i+1,len(a)):
        s+=a[j]
        if s==k:
            print(i,j)
            #print(s)
            break
        elif(s>k):
            s-=a[i]
            i+=1
            j+=1
        else:
            s+=a[j]
            j+=1
"""            
#DAY2- 5th ques- using while (error again)
"""k=int(input())
a=list(map(int,input().split(',')))
s=0
i=0
j=0
while(i<len(a)):
    s+=a[i]
    i+=1
    if s>=k:
        if s==k:
            print(i,j)
        else:
            s-=a[j]
            j+=1
    elif s<k:
        s+=a[i]
"""
#DAY2- 5th ques- working code (error again)
"""
a=list(map(int,input().split(',')))
k=int(input())
s=0
i=0
j=0
flag=0
while(i<len(a)):
    if s<k:
        s+=a[i]
        i+=1
    if s>k:
        while(j<i and s>k):
        #while(s>k):
            s-=a[j]
            j+=1
    if(s==k):
        print(j,i)

"""

#DAY2- 6th ques- len of largest subarray without duplicates
"""
a=list(map(int,input().split(',')))
b=[]
m=0
for i in a:
    if i not in b:
        b.append(i)
    else:
        m=max(m,len(b))
        while(b[0]!=i):
            b.pop(0)
        b.pop(0)
        b.append(i)
m=max(m,len(b))
print(m)

"""


#DAY3- 7th ques- find the longest suarray whose sum is equal to zero (my code)
"""
a=list(map(int,input().split()))
l=0
s=0
d={}
sum_arr=[]
for i in range(0,len(a)):
    s+=a[i]
    sum_arr.append(s)
print(sum_arr)
if(sum_arr[-1]==0):
    print(len(a))
else:
    for i in range(len(sum_arr)):
        if sum_arr[i]==0:
            l=i+1
        if sum_arr[i] not in d:
            d[sum_arr[i]]=i
        else:
            l=max(l,i-d[sum_arr[i]])
print(d)
print(l)
"""
#DAY3- 7th ques- find the longest suarray whose sum is equal to zero (sir's code)
"""
a=list(map(int,input().split()))
l=0
s=0
d={}
for i in range(len(a)):
    s+=a[i]
    if s==0:
        l=i+1
    elif s not in d:
        d[s]=i
    else:
        l=max(l,i-d[s])
print(d)
print(l)
"""
#DAY3- 8th ques- find the longest subarray whose value is equal to k
"""a=list(map(int,input().split()))
d={}
s=0;l=0
for i in range(len(a)):
    """

#DAY3- 8th ques- find the longest subarray whose value is equal to k(taruni's code)
"""
arr=list(map(int,input().split()))
k=int(input())
j,l,s=0,0,0
d={}
while(j<len(arr)):
      s+=arr[j]
      if(s==k):
          l=j+1
      elif((s-k)in d):
          i=s-k
          if(l<j-d[i]):
              l=j+i
      d[s]=j
print(l)
"""          

#RECURSION
#Day 4- 9th ques- gcd using recursion
def gcd(int a,int b):
      if(a==0):
            return b
      r=b%a
      return gcd(r,a)



    




