#STRINGS
#strings are immutable,indexed
#strings allow all 256 characters, unicodes and backslash characters

#valid strings formats
s="vignan"
s="123"
s="a*b"
s="abc@gmail.com"
s="123ab!hell$6??'"
s="hi \n hello \t"

s="vignan 123"
print(s,type(s),len(s))
print(s[-1]) #3
#s[-3]="V"    #immutable

#OPERATIONS
#in java we can concat a string and num but it doesn't work in python
str1="vignan 123"
print(str1, id(str1),type(str1),len(str1))
print(str1[-1])  #3
print(str1[3:6]) #slicing
print("hi"*3)    #hihihi
print("3" in str1)#True

#Concat
str2="college"
str1=str1+" " +str2   #stores str1 in a diff address
print(str1,id(str1))

#FUNCTIONS
s1="vignan institute of technology"

#count()
print(s1.count('a'))  #1

#endswith()
print(s1.endswith('logy'))   #True

#startswith()
print(s1.startswith('vig')) #True

#title()-title function converts every first letter of every word into upper case
caps=s1.title() 
print(caps) #Vignan Institute Of Technology

#swapcase()-swaps all elements into the opposite case(if upper then to lower and vice versa)
print(s1.swapcase())     #VIGNAN INSTITUTE OF TECHNOLOGY

#replace('oldvalue','newvalue')
print(s1.replace('vig','Vig'))    #Vignan institute of technology

#capitalize()---->syntax: s=s.capitalize()
#NOTE= difference between capitalize() and title() is capitalize()n capitalises only first letter of the sentence where as title() capitalises every word's first letter in the sentence
print(s1.capitalize())

#lower()
print(s1.lower())

#upper()
print(s1.upper())

#zfill()- filling zero's in empty spaces
x="hello"
print(x.zfill(10))  #o/p:00000hello

#Generate password
name=input()
name=name.replace(" ","")
dob=input()
phno=input()
print(dob[-4::1]+name[0:4]+phno[-4::1])


#20-11-2024#
#to check string
string1="VIGNAN"
string2="vignan"
string3="VIGNAN123"

string4="hello \n world"
string5="\n"
string6=" "

str1="hiiiiil"
str2="hello hello hello hello hello"
str3="Hi this is harshitha"

print(string1.isupper())
print(string2.islower())

print(string3.isalnum())
print(string3.isalpha())
print(string1.isidentifier())

print(string5.isprintable())
print(string6.isspace())
print(string1.istitle()) #checks if all the first letter in every word is capital

print(str1.index("l"))
print(str2.find("hello"))       #we can pass a string in this whereas in the above method we can't
print(str2.rfind("hello"))        #returns the last occurance of the key in the string
print(str3.index("harsh",9,17 ))  #returns error if value is not found in the given range of index

#split()
xyz="red,green,yellow"
u=xyz.split(",")
print(u,type(u))


#partition()
t1='i love playing video games all day, i usually play video games '
x=t1.partition("video")

#ljust()-padding(left just)
t2="bob"
y=t2.ljust(20," ")s
print(y,"is a writer")
#rjust()-padding(right just)
z=t2.rjust(20," ")
print(z,'is a writer')
      
