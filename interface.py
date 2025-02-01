import sys
import os
import functional
import argparse

commands = {
    'copy': functional.copy_file,
    'delete': functional.delete_file,
    'count': functional.count_files,
    'search': functional.re_search
}

parser = argparse.ArgumentParser(description='CLA File Manager')
subparsers = parser.add_subparsers(dest='command')

# Copy
copy_parser = subparsers.add_parser('copy', help='Copy file')
copy_parser.add_argument('dir', type=str)
copy_parser.set_defaults(func=functional.copy_file)
# Count
count_parser = subparsers.add_parser('count', help='Count files in Dir. Non-recursive')
count_parser.add_argument('dir', type=str)
count_parser.set_defaults(func=functional.count_files)
#Re_search
search_parser = subparsers.add_parser('search', help='Searches files in directory with regular exp. Recursive')
search_parser.add_argument('pattern', type=str)
search_parser.add_argument('-d', '--dir', default = os.getcwd(), help='Directory where to search')
search_parser.set_defaults(func=functional.re_search)

args = parser.parse_args()
print(args)

if args.command == 'search':
    commands[args.command](args.pattern)
else:
    commands[args.command](args.dir)
