#basic syntax
for i in range(1,10,1):
    print(i)
    
#odd
print("odd")
for i in range(1,10,2):
    print(i)

#if no counter then default 1
print("odd")
for i in range(1,10):
    print(i)
    
#-10 to -1
for i in range(-10,0,1):
        print(i)
        
#example of else block in for loop and how it works
for i in range(1,10):
    if(i==3):
        continue
    if(i==5):
        break
    print(i)
else:
    print("cse")

#sum of natural numbers
sum=0
for i in range(1,11):
    sum+=i
print(sum)

#factorial
fact=1
for i in range(1,5):
    fact=fact*i
print(fact)

#factors and sum of factors
n = int(input())
sum =0
for i in range(1,11):
    if(n%i==0):
        print(i)
        sum+=i
print(sum)

#prime number-better logic
n=int(input())
c=0
for i in range(2,(n//2)+1):
    if(n%i==0):
        c+=1
        break
if(c==0):
    print("PRIME")
else:
    print("not prime")
        
