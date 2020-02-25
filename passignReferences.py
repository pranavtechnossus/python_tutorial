import copy
# def eggs(params):
#     params.append('Hello')
#
# spam = [1, 2, 3]
# eggs(spam)
# print(spam)

spam = ['A', 'B', 'C', 'D', 'E']
print('Id Of Spam : ' + str(id(spam)))

# printing id of cheese after copying spam value in it
cheese = copy.copy(spam)
print('Id Of Spam : ' + str(id(cheese)))

cheese[1] = 'Changed'

print(spam)
print(cheese)
