'''
File: main_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''
import sys
sys.path.append("Sender")
from send_GPGLL import generate_messages


def main():
    print("GPGLL Send & Receive Test")
    generate_messages(10)


if __name__ == '__main__':
    main()