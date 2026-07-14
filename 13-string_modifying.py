# string modification


a = "        islamabad is cold city"

b = "        Islamabad is cold city "
print(a)
print(b)
print( a== b )

# LOWER CASE

a = a.lower()
b = b.lower()

print( a== b )

# UPPER CASE

a = a.upper()
b = b.upper()
print( a== b )

# REMOVE WHITESPACE

a=a.strip()
b=b.strip()

print(a)
print(b)

# REPLACE STRING

a = "Hello, World!"
print(a.replace("H", "J"))


# split string

url ="https://www.w3schools.com/python/python_strings_modify.asp"
y =url.split("/")
print(y)