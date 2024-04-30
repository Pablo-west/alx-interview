#!/usr/bin/python3
import sys
import re

def parse_line(line):
    """Parse each line according to the given format."""
    pattern = r'(\d+\.\d+\.\d+\.\d+) - \[(.*?)\] "GET /projects/260 HTTP/1.1" (\d+) (\d+)'
    match = re.match(pattern, line)
    if match:
        return match.groups()
    else:
        return None

def print_statistics(total_size, status_codes):
    """Print statistics."""
    print("File size: {}".format(total_size))
    for code, count in sorted(status_codes.items()):
        print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    lines_processed = 0

    try:
        for line in sys.stdin:
            line = line.strip()
            data = parse_line(line)
            if data:
                status_code = data[2]
                if status_code in status_codes:
                    status_codes[status_code] += 1
                total_size += int(data[3])
                lines_processed += 1

                if lines_processed % 10 == 0:
                    print_statistics(total_size, status_codes)
    except KeyboardInterrupt:
        print_statistics(total_size, status_codes)

if __name__ == "__main__":
    main()
