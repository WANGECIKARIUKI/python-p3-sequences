#!/usr/bin/env python3
def print_fibonacci(length):
    #length is 0 or 1 and use if/elif statement
    if length == 0:
        print([])
        return
    elif length == 1:
        print([0])
        #initialize 2 elments and then use while loop
        return 
    fibonacci_sequence = [0,1]
    while len(fibonacci_sequence)<length:
     next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
    #append fibonacci_sequence
     fibonacci_sequence.append(next_number)

     # print fibonacci_sequence that has been generated
    print(fibonacci_sequence)