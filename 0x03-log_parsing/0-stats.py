#!/usr/bin/python3
import sys

def print_stats(total_size, status_codes):
    """Print statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        if count > 0:
            print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            parts = line.strip().split()
            if len(parts) < 9 or parts[-2] != 'GET' or parts[-4] != 'HTTP/1.1':
                continue

            status_code = parts[-3]
            if status_code not in status_codes:
                continue

            try:
                file_size = int(parts[-5])
            except ValueError:
                continue

            total_size += file_size
            status_codes[status_code] += 1
            lines_processed += 1

            if lines_processed % 10 == 0:
                print_stats(total_size, status_codes)

    except KeyboardInterrupt:
        print_stats(total_size, status_codes)

if __name__ == "__main__":
    main()
