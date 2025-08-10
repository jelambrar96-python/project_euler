from tqdm import tqdm

collatz_dict = {1:1}

def collatz_sequence_length(n):    
    """
    Returns the length of the Collatz sequence starting with n.
    No recursive
    """
    original = n
    length = 0 # if n % 2 == 0 else 2
    while True:
        if n in collatz_dict:
            length += collatz_dict[n]
            break
        if n % 2 == 0:
            n //= 2
            length += 1
        else:
            n *= 3
            n += 1
            n //= 2
            length += 2
    collatz_dict[original] = length
    return length


def longest_collatz_sequence(limit):
    """
    Returns the number under the limit that produces the longest Collatz sequence.
    """
    longest_length = 0
    number_with_longest_sequence = 0

    for i in tqdm(range(1, limit)):
        n = i
        length = collatz_sequence_length(n)

        if length > longest_length:
            longest_length = length
            number_with_longest_sequence = i

    return number_with_longest_sequence

if __name__ == "__main__":
    limit = 1_000_000
    result = longest_collatz_sequence(limit)
    print(f"The number under {limit} that produces the longest Collatz sequence is: {result}")