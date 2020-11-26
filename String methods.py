txt="hello,and welcome to my world"
x=txt.capitalize() #It converts the first character to upper case
print(x)
y=txt.casefold() #It converts the string into lower case
print(y)
z=txt.center(50)#Returns a centered string
print(z)
a=txt.count("welcome",1,18)#returns the number of times that specific value occurs int he string
print(a)
b=txt.endswith("my world",5,11)#Returns value True if it ends with specific value or returns Flase
print(b)
c=txt.find("welcome")#Searches in the string for the specific value and returns the postion
#where it was found .It returns -1 if match not found
print(c)
d=txt.index("welcome")#Similar to find() but it raises a value error if not found
print(d)
e=txt.islower()#Returns True if all the characters is lower case in String or else it returns flase
print(e)
f=txt.isupper()#Returns True if all the characters is in upper case or else it returns False
print(f)
g=txt.istitle()#Returns True if the first word of the character is upper case or else returns false
print(g)
h=txt.isspace()#Returns True if all the characters in a String are whitespaces or gives False
print(h)
i=txt.swapcase()#Swap cases lower case becomes upper case and vice versa
print(i)
j=txt.isalnum()#Returns value True if their exist alphabets and numbers in a string or else False
print(j)
k=txt.isalpha()#Returns value True all the characters in the string are alphabets or else False
print(k)