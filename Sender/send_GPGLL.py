'''
File: send_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

import random
import time

def generate_messages(num):
    utc_time_arr = generate_start_time()

    # Generate Latitude & Longitude

    lat_val = round(9000*random.random(), 4)
    lat_dir = random.choice(['E', 'W'])

    long_val = round(18000*random.random(), 4)
    long_dir = random.choice(['N', 'S'])

    # Update time by adding betwee 0 ms and 1 hour
    utc_time_arr = update_time(utc_time_arr)
    utc_time = 10000*utc_time_arr[0] + 100*utc_time_arr[1] + utc_time_arr[2] + utc_time_arr[3]

    # Generate Mode and Status
    status_number = random.random()
    if status_number <= 0.1:
        status = 'V'
    else:
        status = 'A'

    mode_number = random.random()
    if mode_number <= 0.2:
        mode = 'E'
    elif mode_number <= 0.5:
        mode = 'D'
    else:
        mode = 'A'

    # Generate Checksum
    message = ", ".join(["$GPGLL", str(lat_val), lat_dir, str(long_val), long_dir, str(utc_time), status, mode])
    print(message)

    # Write to file output


def generate_start_time():
    utc_time_h = random.randrange(0, 23)
    utc_time_m = random.randrange(0,59)
    utc_time_s = random.randrange(0,59)
    utc_time_ms = round(random.random(), 3)
    return [utc_time_h, utc_time_m, utc_time_s, utc_time_ms]

def update_time(utc_time_arr):
    utc_time_h = utc_time_arr[0] + random.randrange(0, 5)
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
