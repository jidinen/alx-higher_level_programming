#!/usr/bin/python3


def main():
    """Making a function that takes command line argumets
    Args:
    no



    """
    import sys
    a = 1
    firag = sys.argv[0]
    restag = sys.argv[1:]
    total = len(sys.argv) - 1
    if (total <= 0):
        print("{} argument".format(total))

    elif(total == 1):
        print("{} argument:".format(total))
    else:
        print("{} arguments".format(total))
        for i, arg in enumerate(restag):
            print("{}: {}".format(a, arg))
            a += 1


if __name__ == "__main__":
    main()
