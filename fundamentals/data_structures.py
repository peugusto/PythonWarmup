list = ["car", True, 2, 4.5]
print(type(list))
print(list[3]) #4.5

print("-" * 30)

tuple = ("car", True, 2, 4.5)
print(type(tuple))
print(tuple[0]) #car

print("-" * 30)

dict = {"vehicle":"car", "boolean": True, "int":2,"float":4.5}
print(type(dict))
print(dict["int"]) #2

print("-" * 30)

set = {"car",True,2,3.5}
print(type(set))

# difference between list and tuple -> the list is mutable and the tuple is not, and both are sorted and allows the duplication of values.
# difference between dict and set -> the dict is sorted and mutable, the set is not sorted and not indexed, and both do not allow the duplication of values.