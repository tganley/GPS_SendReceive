'''
File: receive_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

class message_receiver():
    def __init__(self, numMessages):
        self.numMessages = numMessages

    def parse_message(self, line):
        message = message_data()
        message.message = line[:-1] # Remove newline character from end

        components, sep, message.checksum = message.message.partition("*")
        components = components.split(", ")

        message.lat_val = components[1]
        message.lat_dir = components[2]
        message.long_val = components[3]
        message.long_dir = components[4]
        message.utc_time = components[5]
        message.status = components[6]
        message.mode = components[7]
        return message
        

    def receive_messages(self):
        messages = []
        with open("gpgll_messages.txt") as fdes:
            lines = fdes.readlines()

        for i in range(self.numMessages):
            messages.append(self.parse_message(lines[i]))
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
    
    def __eq__(self, other) : 
        return self.__dict__ == other.__dict__
