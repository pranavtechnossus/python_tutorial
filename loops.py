import random
import sys

# While loop
# name = ''
# while not name:
#     print('Enter your name:')
#     name = input()
# print('How many guests will you have')
# numOfGuests = int(input())
# if numOfGuests:
#     print('Be sure to have enough room for all your guests.')
# print('Done.')

# name = 'aa'
# while name != 'a':
#     print("Please type your name")
#     name = input()
# print('Thank you')

# while True:
#     print('Who are you')
#     name = input()
#     if name != 'Pranav':
#         print('Not you please give your right identity')
#         continue
#     print('Hello, Pranav. What is Password ? (it is a fish)')
#     password = input()
#     if password == 'angelfish':
#         break
# print('Access Granted')

# For loop
# range section with one parameter
print('With one parameter')
for i in range(5):
    print('My name iteration : (' + str(i) + ') ')

# range section with two parameter
print('With two parameter')
for i in range(1, 5):
    print('My name iteration : (' + str(i) + ') ')

# range section with two parameter
print('With three parameter')
for i in range(0, 10, 2):
    print('My name iteration : (' + str(i) + ') ')

# range section to count down
print('Counting down')
for i in range(5, 0, -1):
    print('My name iteration : (' + str(i) + ') ')

# total = 0
# for num in range(101):
#     total = total + num
# print(total)

# printing random number using loop
print('\nPrinting random no\n')
for i in range(5):
    print('Random no: ' + str(random.randint(1,10)))

while True:
    print('Type exit to exit.')
    response = input()
    if response == 'exit':
        sys.exit()
    print('You typed ' + response + '.')
