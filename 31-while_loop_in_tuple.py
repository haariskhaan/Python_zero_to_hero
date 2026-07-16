thistuple = ("apple", "banana", "cherry","apple", "banana", "cherry")
i = 0
while i <5:
  print(thistuple[i])
  i = i + 1


total_apple = thistuple.count("apple")
print(total_apple)


tuple1 = ["a", "b" , "c"]
tuple2 = [1, 2, 3]

type(tuple1)


tuple3 = tuple1 + tuple2
print(tuple3)
