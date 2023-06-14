#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""
import sys

total_size = 0
status_codes = {200: 0, 301: 0, 400: 0, 401: 0, 403: 0, 404: 0, 405: 0, 500: 0}
line_count = 0

try:
    for line in sys.stdin:
        # Parse each line of the input
        parts = line.split()
        status_code = int(parts[-2])
        file_size = int(parts[-1])

        # Update metrics
        total_size += file_size
        status_codes[status_code] += 1
        line_count += 1

        # print statistics every 10 lines
        if line_count % 10 == 0:
            print("File size:", total_size)
            for code in sorted(status_codes.keys()):
                if status_codes[code] > 0:
                    print(f"{code}:", status_codes[code])
except KeyboardInterrupt:
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}:", status_codes[code])
    raise
except Exception:
    pass
