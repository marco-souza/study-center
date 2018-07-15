#! env python3
"""This script just print Hello world."""
import sys
from greetings import greeting

if __name__ == "__main__":
    greeting()
    print(sys.argv)
