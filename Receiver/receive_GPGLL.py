'''
File: receive_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

class message_receiver():
    def __init__(self, numMessages):
        self.numMessages = numMessages

    def parse_message(self):
        message = message_data()

        with open("gpgll_messages.txt") as fdes:
            line = fdes.readline()
        components, sep, message.checksum = line.partition("*")
        components = components.split(", ")

        message.lat_val = components[0]
        message.lat_dir = components[1]
        message.long_val = components[2]
        message.long_dir = components[3]
        message.utc_time = components[4]
        message.status = components[5]
        message.mode = components[6]
        return message
        

    def receive_messages(self):
        messages = []
        for i in range(self.numMessages):
            messages.append(self.parse_message())
        return messages

class message_data():
    def __init__(self):
        self.lat_val = 0
        self.lat_dir = ''
        self.long_val = 0
        self.long_dir = ''
        self.utc_time = 0
        self.status = ''
        self.mode = ''
        self.checksum = 0 # Must be =0 for initial checksum condition
        self.message = ''
