from math import log

"""The handshake used by the card and the door involves an operation that transforms a subject number. To transform a 
subject number, start with the value 1. Then, a number of times called the loop size, perform the following steps:

Set the value to itself multiplied by the subject number.
Set the value to the remainder after dividing the value by 20201227."""

def transform(subject_nr, loop_size):
    value = 1
    for _ in range(loop_size):
        #Set the value to itself multiplied by the subject number.
        value = value * subject_nr
        # Set the value to the remainder after dividing the value by 20201227.
        value = value % 20201227
    return value

def find_loop_size(public_key):
    loop_size = 1
    x = loop_size
    while True:
        x = x * 7
        # Set the value to the remainder after dividing the value by 20201227.
        x = x % 20201227
        if x == public_key:
            return loop_size
        loop_size += 1

card_public_key = 5764801
door_public_key = 17807724

card_public_key = 11239946
door_public_key = 10464955


card_loop_size = find_loop_size(card_public_key)
door_loop_size = find_loop_size(door_public_key)
print(card_loop_size)
print(door_loop_size)

encryption_key = transform(card_public_key, door_loop_size)
print(encryption_key)
encryption_key = transform(door_public_key, card_loop_size)
print(encryption_key)