#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    jan = 0
    for i in range(1, len(sys.argv)):
        jan += int(sys.argv[i])
    print("{}".format(jan))
