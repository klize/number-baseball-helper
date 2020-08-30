import argparse
import sys
from number_baseball_helper.helper import NumberBaseballHelper


def define_get_args(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument("--ndigit", type=int, default=4)
    parsed = parser.parse_args(argv)
    return parsed


def main(argv=None):
    args = define_get_args(argv)

    helper = NumberBaseballHelper(ndigit=args.ndigit)
    helper.start_console()


if __name__ == "__main__":
    main(sys.argv[1:])
