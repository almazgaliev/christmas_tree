import sys
from colorama import init
from termcolor import colored
import random as rand
import numpy as np
import argparse

init()  # цвета чтоб нормально отображались на разных осях наскок я понял

colors = ['red',
          'yellow',
          'blue',
          'magenta']


parser = argparse.ArgumentParser(prog="christmas_tree.py",
                                 description='*** draws christmas tree ***')
parser.add_argument('--height', default=21, type=int,
                    help='height of drawn tree (default: %(default)s)')
parser.add_argument('--width', default=-1, type=int,
                    help='width of drawn tree (default: 41')
parser.add_argument('-b', '--balls', nargs='+',
                    default=["0"], help='ball symbols')
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.2 by Almaz Galiev')

args = parser.parse_args(sys.argv[1:])
width = args.width
height = args.height
# make numbers odd
width += (width+1) % 2
height += (height+1) % 2
balls = args.balls


def tree(height, width, ch='*', toys=["0"]):
    spaces = ' '*int(width//2)
    s = spaces + colored("★", "red") + "\n"

    # не понимаю почему тут range(1, height) но пофиг
    for h in range(1, height):
        x = h/height * width

        row = np.array([colored(ch, 'green')] * int(x))
        if len(row) > 2:
            balls = np.random.choice(
                range(1, len(row)-1, 2), rand.randint(0, len(row)-1))
            row[balls] = [colored(rand.choice(toys), rand.choice(colors))
                          for _ in range(len(balls))]
        row = ''.join(row)
        spaces = ' '*int((width - x) / 2)
        s += spaces + row + "\n"
    s += ' ' * (width//2-2) + colored('mWm', 'yellow') + '\n'
    s += ' ' * (width//2-2) + colored('mWm', 'yellow') + '\n'
    return s


def simple_tree(height, ch='*', toys=["o"]):
    spaces = ' '*(height-1)
    s = spaces + colored("★", "red") + "\n"

    for h in range(height):
        row = np.array([colored(ch, 'green')]*int(2*h+1))
        if len(row) > 2:
            balls = np.random.choice(range(1, len(row)-1, 2),
                                     rand.randint(0, len(row)-1))
            row[balls] = [colored(rand.choice(toys), rand.choice(colors))
                          for _ in range(len(balls))]
        row = ''.join(row)

        spaces = ' '*(height-1-h)
        s += spaces + row + "\n"
    s += ' ' * (height-2) + colored('mWm', 'yellow') + '\n'
    s += ' ' * (height-2) + colored('mWm', 'yellow') + '\n'
    return s

if width == -1:
    print(simple_tree(height, toys=balls))
else:
    print(tree(height, width, toys=balls))
