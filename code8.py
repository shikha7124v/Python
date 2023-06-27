# String Methods 

a = "!!Shikha!!!!"
print(len(a))    # length function
print(a)
print(a.upper()) # Upper function
print(a.lower()) # Lower function
print(a.rstrip("!"))  # Function for striping out the given parameters from the end of the string 
print(a.replace("Shikha", "gunnu"))  # Function for replacing any string or character

b = "ab cd"
print(b.split(" "))  # function for splitting out the string via passed parameter

c = "it's me shikha"
print(c.capitalize())

str1 = "Welcome to the console!!!"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))

str2 = "abaabcd"
print(str2.count("a"))
print(str2.endswith("!!!"))
print(a.endswith("!!!"))
print(str2.endswith("b",2,5))

str3 = "He's name is Dan. He is an honest man. "
print(str3.find("is"))
print(str3.find("Dan"))

print(str3.index("am"))
print(str3.isalnum())

str4 = "shikh21"
print(str4.isalnum())

print(str3.isalpha())
print(str2.isalpha())

str5 = "We are here\n"
print(str5.isprintable())
print(str4.isprintable())

print(str3.isspace())

str6 = "   "
print(str6.isspace())

print(str1.istitle())
print(str1.title())