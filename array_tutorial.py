import array  # import array module

# TRAVERSING THE ARRAY
print("TRAVERSING THE ARRAY ")
myArray = array.array('i', [5, 6, 7, 8, 9])
# variable = moduleName.method/classFromModule('dataType',[elements])
print("myArray >>", myArray)
print("array.typecodes >>", array.typecodes)  # displays all the supported type codes
print()

# indexing
print("indexing the array")
print("myArray[-1] >>", myArray[-1])  # the last element
print("myArray[0] >>", myArray[0])
print()

# slicing
print("slicing the array")
print("myArray[1:] >>", myArray[1:])  # everything after the first element
print("myArray[:1] >>", myArray[:1])  # give me only the first element

print("myArray[4:] >>", myArray[4:])  # everything after the first element
print("myArray[::-1] >>", myArray[::-1]) # displays array in reverse order
print("myArray[1::2] >> ", myArray[1::2])
print()

# looping
print("Looping")
print("normal looping")
for i in myArray:
    print(i)
print()
print("loop with slicing")
for i in myArray[3:]:
    print(i)
print()
print("loop with method enumerate() and slicing()")
for i in enumerate(myArray[1::2]):
    print(i)




