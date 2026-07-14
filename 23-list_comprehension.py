list = [1, "pakistan", 3.14, 6, 899, 234]
print(list[0])
print(list[1])
print(list[2])


print(list[-1])

print(list[:3])





# Loop
print("########################### list comprehension using for loop########################")

for item in list:
    print(item)

print("#################################################################################")

list [0] = "bottel"     # replace item in any index
print(list)



list [3] = "cup"
print(list)

print("##################### inserting item #################################")

list2 = []

list2.insert(0, "cup")  # list.insert( index , value)
print(list2)


list2.insert(1, "cup1")
print(list2)


list2.insert(2, "cup2")
print(list2)


("#################################################")

list2.append("cuppppppp")
print(list2)


print("##############################################")
list4 = [1,2,3]
list5 = [4,5,6]

combined_list = list4 + list5
print(combined_list)

combined_list = list4.extend(list5)
print(combined_list)

