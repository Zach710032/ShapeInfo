import argparse
import math

def square(s):

    print('Square Side Length: {}'.format(s))

    area = s * s
    print('  Area: {}'.format(area))

    perimeter = s * 4
    print('  Perimeter: {}'.format(perimeter))


def circle(r):
    
    print('Circle Radius: {}'.format(r))

    circumference = r * 2 * math.pi
    print('  Circumference: {}'.format(circumference))
    
    area = r * r * math.pi
    print('  Area: {}'.format(area))

    
def triangle(b,h):

    print('Triangle Base, Height: {}, {}'.format(b, h))

    area = b * h / 2
    print(  'Area: {}'.format(area))  

def main(args):
    if args.shape == 'square':
        if args.side is not None:
            square(float(args.side))
    if args.shape == 'circle':
        if args.radius is not None:
            circle(float(args.radius))
        elif args.diameter is not None:
            circle(float(args.diameter) / 2 )
    if args.shape == 'triangle':
        if args.base is not None and args.height is not None:
            triangle(float(args.base), float(args.height))
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='SHAPE INFO V 0.2')
    parser.add_argument('shape', choices=['circle','square','triangle'],
                        help='The type of shape to print values for.(triangle is equilateral only)')

    parser.add_argument('--r', dest='radius', required=False)
    parser.add_argument('--d', dest='diameter', required=False)
    parser.add_argument('--s', dest='side', required=False)
    parser.add_argument('--b', dest='base', required=False)
    parser.add_argument('--h', dest='height', required=False)
    
    args = parser.parse_args()

    main(args)
