# list methods
# list functins


# append()	Adds an element at the end of the list
# clear()	Removes all the elements from the list
# copy()	Returns a copy of the list
# count()	Returns the number of elements with the specified value
# extend()	Add the elements of a list (or any iterable), to the end of the current list
# index()	Returns the index of the first element with the specified value
# insert()	Adds an element at the specified position
# pop()	Removes the element at the specified position
# remove()	Removes the item with the specified value
# reverse()	Reverses the order of the list
# sort()	Sorts the list

list_1 = [1,2,3,4,5, "tocheck"]
list_1.append(6)

print(list_1)

print"######################################################"


list_1.clear()
print(list_1)

print"######################################################"

list2 = list_1.copy()
print(list2)

print"######################################################"

my_list = [1, 2, 2, 3]
count = my_list.count(2)
print(count)

list_1 = [1,2,3,4,5, "tocheck"]
a = list_1.count("tocheck")
print(a)

print("use of index ####################################")


index_of_tocheck = list_1.index("tocheck")
print(index_of_tocheck)

print"######################################################"

list_1 = [1,2,3,4,5, "tocheck"]
list_1.insert(0, 7)
print(list_1)

print"######################################################"


list_1 = [1,2,3,4,5, "tocheck"]
list_1.pop()
print(list_1)

print"######################################################"

list_1 = [1,2,3,4,5, "tocheck"]
list_1.remove(5)
print(list_1)

print"######################################################"

list_1 = [1,2,3,4,5, "tocheck"]
list_1.reverse()
print(list_1)

print"######################################################"

list_1 = [1,2,3,4,5, 90,56,23,675,300]
list_1.sort()
print(list_1)

list2 = ["x","a", "b", "c"]
list2.sort()
print(list2)
