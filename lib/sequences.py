#!/usr/bin/env python3

def print_fibonacci(length):
    
    if length <= 0:
        print('[]')
        return
    
    fibonacci_sequence = [0] if length > 0 else []
    a, b = 0, 1
    while len(fibonacci_sequence) < length:
        fibonacci_sequence.append(b)
        a, b = b, a + b
    
    print(fibonacci_sequence)