'''
File: send_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

import random
import time

class message_generator():

    def __init__(self, numMessages):
        self.numMessages = numMessages
        f = open("gpgll_messages.txt", 'w')
        f.close()

    def generate_messages(self):
        print("Generating list of {} messages".format(self.numMessages))
        self.utc_time_arr = self.__generate_start_time()
        for i in range(self.numMessages):
            self.generate_single_message()

    def generate_single_message(self):
        # Generate Latitude & Longitude

        self.lat_val = round(9000*random.random(), 4)
        self.lat_dir = random.choice(['E', 'W'])

        self.long_val = round(18000*random.random(), 4)
        self.long_dir = random.choice(['N', 'S'])

        # Update time by adding betwee 0 ms and 1 hour
        self.utc_time_arr = self.__update_time(self.utc_time_arr)
        self.utc_time = 10000*self.utc_time_arr[0] + 100*self.utc_time_arr[1] + \
            self. utc_time_arr[2] + self.utc_time_arr[3]

        # Generate Mode and Status
        status_number = random.random()
        if status_number <= 0.1:
            self.status = 'V'
        else:
            self.status = 'A'

        mode_number = random.random()
        if mode_number <= 0.2:
            self.mode = 'E'
        elif mode_number <= 0.5:
            self.mode = 'D'
        else:
            self.mode = 'A'

        # Generate Checksum
        self.message = ", ".join(["$GPGLL", str(self.lat_val), self.lat_dir, \
             str(self.long_val), self.long_dir, str(self.utc_time), self.status, self.mode])
        
        self.__calculate_checksum()
        self.message += ('*' + str(self.checksum))

        # Write to file output
        with open("gpgll_messages.txt", 'a') as fdes:
            fdes.write(self.message + '\n')


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

    def __calculate_checksum(self):
        self.checksum = 0
        for character in self.message[1:]:
            self.checksum = self.checksum ^ ord(character)


