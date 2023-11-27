'''
File: send_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

import random
import time
import copy

from receive_GPGLL import message_data

class message_generator():

    def __init__(self, numMessages, error_threshold):
        self.numMessages = numMessages
        f1 = open("Buffers/gpgll_messages.txt", 'w')
        f1.close()
        f2 = open("Buffers/gpgll_err_messages.txt", 'w')
        f2.close()
        self.error_threshold = error_threshold

    def generate_messages(self):
        self.utc_time_arr = self.__generate_start_time()
        message_list = []
        for i in range(self.numMessages):
            message = self.generate_single_message()
            message_list.append(message)
        return message_list


    def generate_single_message(self):
        # Generate Latitude & Longitude
        message = message_data()

        message.lat_val = round(9000*random.random(), 4)
        message.lat_dir = random.choice(['E', 'W'])

        message.long_val = round(18000*random.random(), 4)
        message.long_dir = random.choice(['N', 'S'])

        # Update time by adding betwee 0 ms and 1 hour
        self.utc_time_arr = self.__update_time(self.utc_time_arr)
        message.utc_time = 10000*self.utc_time_arr[0] + 100*self.utc_time_arr[1] + \
            self.utc_time_arr[2] + self.utc_time_arr[3]

        # Generate Mode and Status
        status_number = random.random()
        if status_number <= 0.1:
            message.status = 'V'
        else:
            message.status = 'A'

        mode_number = random.random()
        if mode_number <= 0.2:
            message.mode = 'E'
        elif mode_number <= 0.5:
            message.mode = 'D'
        else:
            message.mode = 'A'

        # Convert and format values into strings
        message.lat_val = "{:09.4f}".format(message.lat_val)
        message.long_val = "{:010.4f}".format(message.long_val)
        message.utc_time = "{:010.3f}".format(message.utc_time)

        # Assemble string message
        self.__assemble_message(message)

        # Assemble version of message with errors
        msg_with_errors = copy.deepcopy(message)
        self.__simulate_errors(msg_with_errors)
        self.__assemble_message(msg_with_errors)

        # Generate and add correct checksum
        checksum = self.calculate_checksum(message)
        message.message = message.message_nochk + '*' + message.checksum
        msg_with_errors.message = msg_with_errors.message_nochk + '*' + message.checksum

        # Write to file output, using the correct messages
        with open("Buffers/gpgll_messages.txt", 'a') as fdes:
            fdes.write(message.message + '\n')

        # Write to file output, using the correct messages
        with open("Buffers/gpgll_err_messages.txt", 'a') as fdes:
            fdes.write(msg_with_errors.message + '\n')
        
        return message


    def __generate_start_time(self):
        utc_time_h = random.randrange(0, 23)
        utc_time_m = random.randrange(0,59)
        utc_time_s = random.randrange(0,59)
        utc_time_ms = round(random.random(), 3)
        return [utc_time_h, utc_time_m, utc_time_s, utc_time_ms]

    def __update_time(self, utc_time_arr):
        utc_time_h = utc_time_arr[0] + random.randrange(0, 3)
        if utc_time_h >= 24:
            utc_time_h -= 24

        utc_time_m = utc_time_arr[1] + random.randrange(0,59)
        if utc_time_m >= 60:
            utc_time_m -= 60

        utc_time_s = utc_time_arr[2] + random.randrange(0,59)
        if utc_time_s >= 60:
            utc_time_s -= 60

        utc_time_ms = utc_time_arr[3] + round(random.random(), 3)
        if utc_time_ms >= 1000:
            utc_time_ms -= 1000
        return [utc_time_h, utc_time_m, utc_time_s, utc_time_ms]
    
    def __assemble_message(self, message):
        message.message_nochk = ", ".join(["$GPGLL", message.lat_val, message.lat_dir, \
            message.long_val, message.long_dir, message.utc_time, message.status, message.mode])


    def calculate_checksum(self, message):
        message.checksum = 0
        for character in message.message_nochk[1:]:
            message.checksum = message.checksum ^ ord(character)
        message.checksum = "{:03}".format(message.checksum)
        return message.checksum

    def __simulate_errors(self, message):
    # Simulate some chance of discrepancies arising
        if(random.random() < self.error_threshold):
            message.lat_val = str(round(float(message.lat_val) + 9000*random.random(),4))
        if(random.random() < self.error_threshold):
            message.long_val = str(round(float(message.long_val) + 18000*random.random(), 4))
        if(random.random() < self.error_threshold):
            message.checksum = str(int(message.checksum) + random.randrange(0,10))


