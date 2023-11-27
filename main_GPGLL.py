'''
File: main_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''
import sys
import random
sys.path.append("Sender")
sys.path.append("Receiver")
from send_GPGLL import message_generator
from receive_GPGLL import message_receiver

NUM_MESSAGES = 40 # Number of messages to generate, send, and check
ERROR_THRESHOLD = 0.1 # Higher index means more generated errors. 0 < index < 1

def test_compareSentAndReceived(sent_messages, received_messages):
    print("\nComparing sent and received messages")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        if sent_messages[i] == received_messages[i]:
            num_successes += 1
        else:
            print("ERROR in message {}: sent {}\n but received {}".format(i, sent_messages[i].message, received_messages[i].message))
    print("{}/{} messages were successfully received\n".format(num_successes, NUM_MESSAGES))

def test_validateChecksums(received_messages):
    print("\nVerifying checksums in received messages")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        old_checksum = received_messages[i].checksum
        recalc_checksum = message_generator.calculate_checksum(0, received_messages[i])
        if old_checksum == recalc_checksum:
            num_successes += 1
        else:
            print("ERROR in message {}: Calculated checksum = {}, but received {}\n".format(i, recalc_checksum, old_checksum))
    print("{}/{} checksums were correct\n".format(num_successes, NUM_MESSAGES))

def test_validateLatLongs(received_messages):
    print("\nVerifying latitude and longitude values")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        if 0 <= float(received_messages[i].lat_val) <= 9000 and 0 <= float(received_messages[i].long_val) <= 18000:
            num_successes += 1
        else:
            print("ERROR in message {}: (lat, long) = ({}, {}) is outside of bounds".format(i, received_messages[i].lat_val, received_messages[i].long_val))
    print("{}/{} lat/long pairs were valid\n".format(num_successes, NUM_MESSAGES))


def main():
    print("GPGLL Send & Receive Test")

    # Create messages
    generator = message_generator(NUM_MESSAGES, ERROR_THRESHOLD)
    sent_messages = generator.generate_messages()

    # Receive and parse messages from file buffer
    receiver = message_receiver(NUM_MESSAGES)
    received_messages = receiver.receive_messages()

    # Test results against expected values
    test_compareSentAndReceived(sent_messages, received_messages)
    test_validateChecksums(received_messages)
    test_validateLatLongs(received_messages)



if __name__ == '__main__':
    main()