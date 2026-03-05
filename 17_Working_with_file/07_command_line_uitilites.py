# Creating Command Line Utilities
# You can use Python to create simple command-line utilities. The argparse module makes it easier to handle command-line arguments.

import argparse
parser=argparse.ArgumentParser(description="A Simple Command Line Utilities")

parser.add_argument("num1",type=float,help="first Number")
parser.add_argument("num2",type=float,help="second Number")
parser.add_argument("operation",choices=["add","sub","mul","div"],help="Operators to perform")

args=parser.parse_args()
print(args)


if args.operation=="add":
    print(f"The Result Is:{args.num1+args.num2}")
elif args.operation=="sub":
    print(f"The Result Is :{args.num1-args.num2}")
elif args.operation=="mul":
    print(f"The Result Is:{args.num1*args.num2}")
elif args.operation=="div":
    print(f"The Result Is:{args.num1/args.num2}")
else:
    print("Some Error Occurred")