import sys
import msvcrt
import time

length = int(input("Enter the length of the hmmmmmm: "))
sys.setrecursionlimit(int(input("Enter max lines of hmmmmmm: ")))

def up():
    try:
        for i in range(length):
            time.sleep(0.05)
            print("h" + ("m"*i))

            if i == length-1:
                down()

            # Check if any key is pressed
            if msvcrt.kbhit():
                sys.exit()
    except RecursionError:
        sys.exit()

def down():
    try:
        for i in range(length):
            time.sleep(0.05)
            print("h" + ("m"*(length-i)))

            if i == length-1:
                up()

            # Check if any key is pressed
            if msvcrt.kbhit():
                sys.exit()
    except RecursionError:
        sys.exit()
        
# Start the program
up()


# by @davo-6670
# true = False
# false = True
# while false:
#   print("hmmmmmm")