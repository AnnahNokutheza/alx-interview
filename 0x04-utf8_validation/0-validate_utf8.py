#!/usr/bin/python3
"""
def validUTF8(data):
    def get_num_bytes(byte):
        # Count the number of leading '1's in the byte to determine the number of bytes in the character.
        for i in range(7, 0, -1):
            if not byte & (1 << i):
                return 7 - i
        return 0

    i = 0
    while i < len(data):
        # Get the number of bytes for the current character
        num_bytes = get_num_bytes(data[i])

        # Check if the number of bytes is within the valid range (1 to 4 bytes)
        if num_bytes not in [1, 2, 3, 4]:
            return False

        # Check if there are enough remaining bytes in the data set
        if len(data) - i - 1 < num_bytes:
            return False

        # Check if the next bytes start with the binary pattern '10xxxxxx'
        for j in range(i + 1, i + num_bytes + 1):
            if data[j] >> 6 != 0b10:
                return False

        i += num_bytes + 1

    return True

# Test cases
print(validUTF8([197, 130, 1]))  # True (represents two valid characters: 'Â' and '\x01')
print(validUTF8([235, 140, 4]))  # True (represents a valid character: '日')
print(validUTF8([240, 144, 128, 128]))  # True (represents a valid character: '𐀀')
print(validUTF8([197, 130, 100]))  # False (invalid UTF-8 sequence)
print(validUTF8([235, 140]))  # False (incomplete UTF-8 sequence)
