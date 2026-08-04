d stdin line by line and compute metrics from an HTTP log stream.

Every 10 lines, and on keyboard interruption (CTRL+C), print:
    - the total file size accumulated so far
    - the number of lines seen per status code (only for codes that
      appeared at least once), in ascending order
"""
import sys


def print_stats(total_size, status_codes):
    """Print the accumulated file size and status code counts."""
    print("File size: {}".format(total_size))
    for code in sorted(status_codes.keys()):
        print("{}: {}".format(code, status_codes[code]))


if __name__ == "__main__":
    valid_codes = {"200", "301", "400", "401", "403", "404", "405", "500"}
    total_size = 0
    status_codes = {}
    line_count = 0

    try:
        for line in sys.stdin:
            parts = line.split()

            # Need at least a status code and a file size as the last
            # two fields to consider the line usable at all.
            if len(parts) < 2:
                continue

            try:
                size = int(parts[-1])
            except ValueError:
                continue

            # File size always counts once we can parse it.
            total_size += size

            status = parts[-2]
            if status in valid_codes:
                status_codes[status] = status_codes.get(status, 0) + 1

            line_count += 1
            if line_count % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)
        raise

    else:
        print_stats(total_size, status_codes)
