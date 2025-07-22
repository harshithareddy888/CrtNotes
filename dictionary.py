#DICTIONARY
#dictionary is unordered according to the books but as the version of python changes it changes so it is ordered in newer versions
#dict is unindexed but we use keys as indices
#empty dictionary

d={}

d={"name":"harshitha","roll":88,"branch":"cse"}
print(d,type(d))

d1={"e1":[65,66,67],"e2":[80,89,800]}
print(d1,type(d1))

#methods

d={"a":5,"b":6,"c":7}
print(*d.keys())
print(*d.values())
print(d.items())


for i in d.values():
    i=i*10  #temporary cahnges will be made
    print(i)
    
for k in d.keys():
    print(k)

for k,v in d.items():
    print(k,"@",v*10)  
print(d)
for k,v in d.items():
    d[k]=v*10
print(d)
    

a={1:10,2:20}
print(a)
a.update({3:44,2:22})
print(a)

#CONCAT DICTIONARY
d1={1:2,3:5}
d2={5:6,7:8}
d3={}
for i in (d1,d2):
    d3.update(i)
print(d3)

#READING I/P:
#i/p={'a':3,'b':5}
d1=eval(input())

#i/p=[a,b,c,d] [1,2,3,4]
#o/p={'a':1,'b':2,'c':3,'d':4}
d={}
i=0
for k in l1:
    d[k]=l2[i]
    i=i+1
print(d)

#excerise
#s:"vignan vits"
#o/p:{'v':2,'i':2,'g':1,'n':2,'a':1,'t':1,'s':1}

d={}
s=input()
k=set(s)  #vignats
for i in k:
    d[i]=s.count(i)
print(d)
