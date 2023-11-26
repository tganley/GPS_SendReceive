'''
File: receive_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

class message_receiver():
    def __init__(self, numMessages):
        self.numMessages = numMessages

    def parse_message(self):
        with open("gpgll_messages.txt") as fdes:
            message = fdes.readline()
        components, sep, checksum = message.partition("*")
        components = components.split(", ")
        print(components)

    def receive_messages(self):
        self.parse_message()