#!/usr/bin/python3

import sys


def print_statistics(status_codes, total_file_size):
    """
    Prints the statistics.
    
    Args:
        status_codes (dict): Dictionary containing the count of status codes.
        total_file_size (int): Total file size.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(status_codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def main():
    total_file_size = 0
    counter = 0
    status_codes = {
        "200": 0,
        "301": 0,
        "400": 0,
        "401": 0,
        "403": 0,
        "404": 0,
        "405": 0,
        "500": 0
    }

    try:
        for line in sys.stdin:
            parsed_line = line.split()
            parsed_line = parsed_line[::-1]  # Reverse the parsed line to get the desired fields

            if len(parsed_line) >= 2:
                counter += 1

                if counter <= 10:
                    total_file_size += int(parsed_line[0])  # File size
                    status_code = parsed_line[1]  # Status code

                    if status_code in status_codes:
                        status_codes[status_code] += 1

                if counter == 10:
                    print_statistics(status_codes, total_file_size)
                    counter = 0

    except KeyboardInterrupt:
        pass  # Handle keyboard interruption gracefully

    finally:
        print_statistics(status_codes, total_file_size)
        sys.exit(0)


if __name__ == "__main__":
    main()
