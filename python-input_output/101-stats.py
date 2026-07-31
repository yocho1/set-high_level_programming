#!/usr/bin/python3
"""Script that reads stdin and computes metrics."""
import sys
import re


def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parse a log line and return status code and file size if valid."""
    parts = line.split()

    # Check if line has at least 7 parts (IP, -, date, request, status, size)
    if len(parts) < 7:
        return None, None

    # Check if status code is valid (must be an integer)
    try:
        status_code = int(parts[-2])
    except ValueError:
        return None, None

    # Check if file size is valid (must be an integer)
    try:
        file_size = int(parts[-1])
    except ValueError:
        return None, None

    # Only accept valid status codes
    if status_code not in [200, 301, 400, 401, 403, 404, 405, 500]:
        return None, None

    return status_code, file_size


def main():
    """Main function to process stdin and compute metrics."""
    total_size = 0
    status_codes = {
        200: 0, 301: 0, 400: 0, 401: 0,
        403: 0, 404: 0, 405: 0, 500: 0
    }
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            status_code, file_size = parse_line(line)

            if status_code is not None:
                status_codes[status_code] += 1
                total_size += file_size

            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    print_stats(total_size, status_codes)


if __name__ == "__main__":
    main()
