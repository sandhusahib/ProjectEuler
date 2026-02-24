"""Finds starting number that produces the longest chain for 
    the Collatz Problem with starting number under 1 million"""

max_seq_length = 0
start_max_seq = 0

for starting_number in range(1, 10**6):
    sequence_length = 1
    term = starting_number
    while term > 1 or (term == 1 and sequence_length == 1):
        if term % 2 == 0:
            term = term/2
        else:
            term = 3*term + 1
        sequence_length += 1

    if sequence_length > max_seq_length:
        max_seq_length = sequence_length
        start_max_seq = starting_number

print((start_max_seq, max_seq_length))