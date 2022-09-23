#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args = len(sys.argv)
    j = 0
    for i in range(1, args):
        j += int(args[i])
    print("{}".format(j))
