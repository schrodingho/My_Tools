import sys
import argparse
parser=argparse.ArgumentParser()
parser.description='do calculation'
parser.add_argument("NumA",help='A',type=int)
parser.add_argument("NumB",help='B',type=int)
args=parser.parse_args()
print(f"Result {args.NumA+args.NumB}")



