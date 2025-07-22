n=input()
ans=''
for i in range(len(n)):
    ans=str(n%10)
    if(ans%2==0):
        ans=int(ans)+1
    else:
        ans=int(ans)-1
    n//=10
print(int(ans))

