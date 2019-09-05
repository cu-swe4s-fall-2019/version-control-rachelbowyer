import argparse
import math_lib as ml
import sys


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Nums to Add and Divide")
    parser.add_argument('oper', type=str, help='choose div or add')
    parser.add_argument('a', type=float, help='any real number')
    parser.add_argument('b', type=float, help='any real number')
    args = parser.parse_args()

    if args.oper == 'add':
        print(ml.add(args.a, args.b))
    elif args.oper == 'div':
        print(ml.div(args.a, args.b))
    else:
        print("Must specify add or div only")
        sys.exit(1)
