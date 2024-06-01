import argparse

parser = argparse.ArgumentParser(description='Process some inputs.')
parser.add_argument('--number', type=int, help='process a number')
parser.add_argument('--text', type=str, help='process some text')
parser.add_argument('--flag', action='store_true', default=False,
                    help='set a flag')
parser.add_argument('files', nargs='*', help='process one or more files')

args = parser.parse_args()

if args.number is not None:
    print(f"Processing number: {args.number}")
if args.text is not None:
    print(f"Processing text: {args.text}")
if args.flag:
    print("Flag is set")
if args.files:
    print(f"Processing {len(args.files)} file(s): {', '.join(args.files)}")
