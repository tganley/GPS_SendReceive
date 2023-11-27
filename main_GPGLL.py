'''
File: main_GPGLL.py
Author: Thomas Ganley
Date: November 26, 2023
'''
import sys
sys.path.append("Sender")
sys.path.append("Receiver")
from send_GPGLL import message_generator
from receive_GPGLL import message_receiver

NUM_MESSAGES = 10

def test_compareSentAndReceived(sent_messages, received_messages):
    print("\nComparing sent and received messages")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        if sent_messages[i] == received_messages[i]:
            num_successes += 1
    print("{}/{} messages were successfully received\n".format(num_successes, NUM_MESSAGES))

def test_validateChecksums(received_messages):
    print("\nVerifying checksums in received messages")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        recalc_checksum = message_generator.calculate_checksum(0, received_messages[i])
        if received_messages[i].checksum == recalc_checksum:
            num_successes += 1
    print("{}/{} checksums were correct\n".format(num_successes, NUM_MESSAGES))

def test_validateLatLongs(received_messages):
    print("\nVerifying latitude and longitude values")
    print("------------------------------------------")
    num_successes = 0
    for i in range(NUM_MESSAGES):
        if 0 <= float(received_messages[i].lat_val) <= 9000 and 0 <= float(received_messages[i].long_val) <= 18000:
            num_successes += 1
    print("{}/{} lat/long pairs were valid\n".format(num_successes, NUM_MESSAGES))



def main():
    print("GPGLL Send & Receive Test")
    generator = message_generator(NUM_MESSAGES)
    sent_messages = generator.generate_messages()

    receiver = message_receiver(NUM_MESSAGES)
    received_messages = receiver.receive_messages()

    test_compareSentAndReceived(sent_messages, received_messages)
    test_validateChecksums(received_messages)
    test_validateLatLongs(received_messages)



if __name__ == '__main__':
    main()