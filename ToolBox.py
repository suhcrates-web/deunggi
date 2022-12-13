import sys


def header_reader():
    x = sys.stdin.readlines()

    header = {}
    for line in x:
        line = line.strip() + ' '
        # print(line)
        a, b = line.split(': ')
        # print(len(a))
        # print(a)
        # print(a)

        header[a] = b.strip()
    return header

print(header_reader())