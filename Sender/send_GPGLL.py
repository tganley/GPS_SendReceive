'''
File: send_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''

import random
import time

utc_time = time.time()

# Generate Latitude & Longitude

lat_val = round(180*random.random(), 4)
lat_dir = random.choice(['E', 'W'])

long_val = round(180*random.random(), 4)
long_dir = random.choice(['N', 'S'])

# Update time by adding betwee 0 ms and 1 hour
utc_time = utc_time + random.randrange(0, 3600) + round(random.random(), 3)

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

# Write to file output
