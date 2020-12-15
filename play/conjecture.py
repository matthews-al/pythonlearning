"""
Collatz Conjecture - Start with a number n > 1. Find the number of steps it
takes to reach one using the following process:
 If n is even, divide it by 2.
 If n is odd, multiply it by 3 and add 1.
"""
import sys

def usage():
    """ print usage """
    print("This script tests the Collatz Conjecture.")
    print("Call with a single integer greater than 1")

def collatz(val=1):
    """ Step count the collatz conjecture, return count """
    count = 0
    while val > 1:
        count += 1
        if val % 2 == 0: # If even, divide by 2
            val = val / 2
        else:  # If odd, multiply by 3 + 1
            val = val * 3 + 1

        if count > 5000:  # Protect from infinite run
            break
    return count

if __name__ == "__main__":
    if len(sys.argv) < 2:
        usage()
        sys.exit(1)

    if not sys.argv[1].isnumeric():
        usage()
        sys.exit(2)

    num = int(sys.argv[1])
    if num < 1:
        usage()
        sys.exit(3)

    print(f"Testing: {num}")
    print(f"{num} took {collatz(num)} collatz steps to reach 1")
