# animals = ['fat','cat','bat','rat']
#
# # print(animals[0:-1])
# # for loop
# # for index in range(4):
# #     print(animals[index])
#
#
# # for each loop
# # for val in animals:
# #     print(val)
#
# # nested array
# spam = [['cat', 'bat'], [10, 20, 30, 40, 50]]
# #
# # print(len(animals))
# #
# # animals[0] = 'Inserted Animal'
# #
# # animals[1] = animals[0]
#
# newList = animals + spam
# print('Before deletion')
# print(newList)
# # del newList[3] # del statement is good to use when you know the index of the value you want to remove from the list
# print('After deletion')
# print(newList[1:2])
# print(len(newList))
# print(newList.index('fat'))  # to find index of any value
# newList.insert(4, 'newItemInserted')
# print(newList)
# newList.append('New Append Data')
# print(newList)

newList = []

for item in range(6):
    if item == 0:
        newList.insert(item, 'First Item')
    if item == 1:
        newList.insert(item, 'Second Item')
    if item == 2:
        newList.insert(item, 'Third Item')
    if item == 3:
        newList.insert(item, 'Fourth Item')
    if item == 4:
        newList.insert(item, 'Fifth Item')
    if item == 5:
        newList.insert(item, 'First Item')

print(newList)
print('After removing from array')
newList.remove('First Item') # this method is useful when you know the value you want to remove from the list.
print(newList)
