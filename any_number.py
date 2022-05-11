#!/usr/bin/env python3

# Created by Devin Jhu
# Created on May 2022
# The loop multiplier


def main():
    # this program shows the sum of number entered
    counter = 0
    sum = 0

    # input
    number = input("Enter number (integer): ")

    # process & output
    try:
        number_int = int(number)
        if number_int <= 0:
            print("Not a positive number")
        else:
            for counter in range(number_int + 1):
                sum = counter * counter
                print("{0}² = {1}".format(counter, sum))

    except Exception:
        print("Not a number.")
    print("\nDone.")


if __name__ == "__main__":
    main()
