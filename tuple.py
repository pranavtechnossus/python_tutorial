stringArray = ('hello Tuple', 0.5, 12)
listedValues = ['12','21','22','34']
print(stringArray)
print(len(stringArray))
print(stringArray[1:3])
# stringArray[0] = 'Hello Another'
# print(stringArray)
anothertuple = ('SecondValue')
print(anothertuple)
anothertuple1 = ('SecondValue',)
print(anothertuple1)

# converting from list to tuples and tuples to list

print(list(('cat','dog','5,','03.1')))
print(list(anothertuple))

print(tuple(listedValues))

# Identity and the id() Function

print(id('Howdy Dude'))
fullName = 'Pranav'
# printing first memory allocation
print(id(fullName))
fullName += 'Verma'
# printing new memory allocation
print(id(fullName))

eggs = ['cat', 'dog'] # This creates a new list.
print(id(eggs))
eggs.append('moose') # when we append something in existing list it doesnt change the id it still refers to same list
print(id(eggs))

eggs = ['cat', 'dog', 'moose'] #  This creates a new list, which has a new identity.
print(id(eggs))



#Python’s automatic garbage collector deletes any values not
# being referred to by any variables to free up memory.
# You don’t need to worry about how the garbage collector works,
# which is a good thing: manual memory management in other programming languages is a common source of bugs.
