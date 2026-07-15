thislist = ["apple", "banana", "cherry"]

length  =  len(thislist)

if length > 0:
    print(length)
    thislist.pop()
    length = length-1

print("now list is ", thislist)