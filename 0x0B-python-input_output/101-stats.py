#!/usr/bin/python3
"""script that reads stdin line by line and computes metrics
"""


def print_statistics(total_size, status_codes):
    """print statistics every 10 lines"""
    print("File size:", total_size)
    for code in sorted(status_codes.keys()):
        print(f"{code}: {status_codes[code]}")


if __name__ == "__main__":
    import sys

    total_size = 0
    valid_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            if line_count == 10:
                print_statistics(total_size, status_codes)
                line_count = 1
            else:
                line_count += 1

            parts = line.split()

            try:
                total_size += int(parts[-1])
            except (IndexError, ValueError):
                pass

            try:
                if parts[-2] in valid_codes:
                    """get returns -1 if key:value doesn't exist"""
                    if status_codes.get(parts[-2], -1) == -1:
                        status_codes[parts[-2]] = 1
                    else:
                        status_codes[parts[-2]] += 1
            except IndexError:
                pass
        print_statistics(total_size, status_codes)

    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)
        raise
