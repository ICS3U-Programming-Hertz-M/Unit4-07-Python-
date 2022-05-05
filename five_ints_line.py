# !/usr/bin/env python3

# created by Hertz Antonella
# created on may,5, 2022
# This program print a new line evry time the number is
# divisible  by 5 0r equal to 1000


def main():
    
    # display numbers from 1000 to 2000 to the user.
    for counter in range(1000, 2001):
        if counter % 5 == 0 and counter != 1000:
            print("")
        print(counter, "", end="")


if __name__ == "__main__":
    main()
