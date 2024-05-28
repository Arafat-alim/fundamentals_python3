# string data type

# literal assignment
first = "Arafat"
last = "Alim"

# print(type(first)) # <class 'str'>
# print(type(first) == str) # true
# print(isinstance(first, str)) # true

# constructor function
pizza = str("Macroni")
print(type(pizza)) # <class 'str'>
print(type(pizza) == str) # true
print(isinstance(pizza, str)) # true

# concat 
fullname = first + " " + last
print(fullname) # Arafat Alim

fullname += "!"
print(fullname) # Arafat Alim!

# casting a number to a string
decade = str(1997)
print(type(decade)) # <class 'str'>
print(decade) # 1997

statement = "I was born in " + decade
print(statement) # I was born in 1997

# multi line string
multiLine = '''
Hello! I am Arafat Alim!    
                Looking for a good opportunity somewhere.
                
'''
print(multiLine)

# Escape special character
special = 'I\'m back at work!\t Hey\nBrother'
print(special)



