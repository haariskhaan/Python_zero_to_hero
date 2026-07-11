# string comprehension using loops


a = "Haris is good freelancer HHHHHHHHHH"
b = a[:]
print (a)
count = 0


for f in a:
    if f=="H":
        count = count + 1

print(count)


# how to find length of string

lengthe_of_string = len(a)

print (lengthe_of_string)

# how to check either word is pressent in string or not

txt = "The best things in life are free!"

yes_no  = "haris" in txt
print (yes_no)


yes_no  = "haris" in "haris is klsjdfkldsjlfkasl"
print (yes_no)