#!/usr/bin/python3
"""Script that reads stdin and computes metrics."""
import sys


def print_stats(total_size, status_codes):
    """Print the current statistics."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print("{}: {}".format(code, status_codes[code]))


def parse_line(line):
    """Parse a log line and return status code and file size if valid."""
    parts = line.split()

    # Need at least 7 parts for a valid log line
    if len(parts) < 7:
        return None, None

    # Try to get status code (second to last)
    try:
        status_code = int(parts[-2])
    except (ValueError, IndexError):
        return None, None

    # Try to get file size (last)
    try:
        file_size = int(parts[-1])
    except (ValueError, IndexError):
        return None, None

    # Only accept valid status codes
    valid_codes = {200, 301, 400, 401, 403, 404, 405, 500}
    if status_code not in valid_codes:
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
