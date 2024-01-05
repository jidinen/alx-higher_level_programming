#!/usr/bin/python3


def main():

    """ A function that adds numbers infinitly


    """
    import sys
    start_arg = sys.argv[0]
    counter = 0
    for i in sys.argv[1:]:
        counter += int(i)

    print("{}".format(counter))


if __name__ == "__main__":
    main()
