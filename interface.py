import sys
import os
import functional
import argparse

commands = {
    'copy': functional.copy_file,
    'delete': functional.delete_file,
    'count': functional.count_files
            }

parser = argparse.ArgumentParser(description='CLA File Manager')
subparsers = parser.add_subparsers(dest='command')

# Copy
copy_parser = subparsers.add_parser('copy', help='Copy file')
copy_parser.add_argument('og_file', type=str)

# Count
count_parser = subparsers.add_parser('count', help='Count files in Dir. Non-recursive')
count_parser.add_argument('dir', type=str)
args = parser.parse_args()

commands[args.command](args.dir)
