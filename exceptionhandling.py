def divide(divide_by):
    try:
        return 42/divide_by
    except ZeroDivisionError:
        print('Error: Invalid Argument')


# Division by 2
print(divide(2))
# Division by 4
print(divide(4))
# Division by 0 to generate Exception and Handle
print(divide(0))
# Division by 5
print(divide(5))
