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

def main():
    print("GPGLL Send & Receive Test")
    generator = message_generator(NUM_MESSAGES)
    sent_messages = generator.generate_messages()

    receiver = message_receiver(NUM_MESSAGES)
    received_messages = receiver.receive_messages()



if __name__ == '__main__':
    main()