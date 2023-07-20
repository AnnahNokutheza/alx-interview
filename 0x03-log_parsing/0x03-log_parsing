#!/usr/bin/python3
import sys

# Function to print statistics based on current data
def print_statistics(file_sizes, status_codes):
    total_size = sum(file_sizes)
    print(f"Total file size: {total_size}")

    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")

# Initialize variables to store data
file_sizes = []
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    # Read input from stdin line by line
    for line in sys.stdin:
        line_count += 1

        # Parse the line to get relevant data
        parts = line.strip().split()
        if len(parts) != 7:
            continue

        ip_address, _, _, method, _, status_code, file_size = parts

        if method != 'GET':
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        # Update statistics
        file_sizes.append(file_size)
        status_codes[status_code] += 1

        # Print statistics after every 10 lines
        if line_count % 10 == 0:
            print_statistics(file_sizes, status_codes)

except KeyboardInterrupt:
    # Handle keyboard interruption (CTRL + C)
    print_statistics(file_sizes, status_codes)
