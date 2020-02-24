import time, sys

def makepattern():
    indent = 0
    indentIncreasing = True

    while True:
        print(' ' * indent, end='')
        print('********')
        time.sleep(0.1) # Pause for 1/10 of a second.
        if indentIncreasing:
            indent = indent + 1
            if indent == 20:
                indentIncreasing = False

makepattern()
