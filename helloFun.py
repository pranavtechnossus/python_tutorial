import random
# def hello():
#     print('Howdy!')
#     print('Howdy!')
#     print('Howdy!')
# hello()
#
#
# def helloName(name):
#     print('Hello ' + name)
#
# helloName('Pranav Called From Function')
#
#



def getAnswer(numberKey):
    if numberKey == 1:
        return 'It is certain'
    if numberKey == 2:
        return 'It is not certain'
    if numberKey == 3:
        return 'It is certain'
    if numberKey == 4:
        return 'It is magic'
    if numberKey == 5:
        return 'You are devil'
    if numberKey == 6:
        return 'It is horrible'
    if numberKey == 7:
        return 'It is wrong'
    if numberKey == 8:
        return 'It is not in your destiny'


r = random.randint(1, 9)
fortune = getAnswer(r)
print(fortune)

# to remove the new line in case using two print()
print('Hello', end='')
print('World')


print('cats', 'dogs', 'mice')
print('cats', 'dogs', 'mice', sep=',')
