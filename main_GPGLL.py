'''
File: main_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''
import sys
sys.path.append("Sender")
from send_GPGLL import message_generator


def main():
    print("GPGLL Send & Receive Test")
    generator = message_generator(numMessages = 10)
    generator.generate_messages()


if __name__ == '__main__':
    main()