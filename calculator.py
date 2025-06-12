import operator
import argparse

ops = {
    'add': operator.add,
    'sub': operator.sub,
    'mul': operator.mul,
    'div': operator.truediv,
}

def main():
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument('x', type=float, help='First operand')
    parser.add_argument('op', choices=ops.keys(), help='Operation')
    parser.add_argument('y', type=float, help='Second operand')
    args = parser.parse_args()
    func = ops[args.op]
    result = func(args.x, args.y)
    print(result)

if __name__ == '__main__':
    main()
