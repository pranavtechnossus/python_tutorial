import random

unsortedNumberArray = []
unsortedStringArray = ['John','Kevin','Zalda','Hamiz',' Michael','Anna','Dynamo']
userName = 'PranavKumar'
for value in range(10):
    unsortedNumberArray.append(random.randint(1, 20))
# unsorted array
print(unsortedNumberArray)

# sorted array
unsortedNumberArray.sort()
print(unsortedNumberArray)
unsortedStringArray.sort()
print(unsortedStringArray)

# reverse array
unsortedNumberArray.reverse()
print(unsortedNumberArray)
unsortedStringArray.reverse()
print(unsortedStringArray)
# printing randomly
print(unsortedStringArray[random.randint(0, len(unsortedStringArray))])

# strings and lists are actually similar if you consider a string to be a “list” of single text characters
# The Python sequence data types include lists, strings, range objects returned by range()
# Many of the things you can do with lists can also be done with strings and other values of sequence types: indexing; slicing; and using them with for loops, with len()
# for example
print(userName)
# for item in userName:
#     print(item) string values are immutable and lists are mutable capable of changing
print(userName[5])
for i in userName:
    print('**' + i + '**')

# so for updating string value we can concatinate or slice and build a new string for example:
newName = userName[0:11]+'Verma'
print(newName)
