import os
import functional
import argparse


def parse_args(args_list=None):
    """
    Принимает на себя аргументы и парсит их
    """
    parser = argparse.ArgumentParser(description='CLA File Manager')
    subparsers = parser.add_subparsers(dest='command', required=True)

    # Copy
    copy_parser = subparsers.add_parser('copy', help='Copy file. Takes path/file name and makes copy of it in current dir')
    copy_parser.add_argument('dir', type=str, help='Path or file name')
    copy_parser.set_defaults(func=functional.copy_file)
    # Delete
    delete_parser = subparsers.add_parser('delete', help='Delete file. Takes path/file name and deletes it')
    delete_parser.add_argument('dir', type=str, help='Path/file name')
    delete_parser.set_defaults(func=functional.delete_file)
    # Count
    count_parser = subparsers.add_parser('count', help='Takes dir and returns amount of files there')
    count_parser.add_argument('dir', type=str, help='Dir where to count')
    count_parser.set_defaults(func=functional.count_files)
    # Re_search
    search_parser = subparsers.add_parser('search', help='Searches files in directory with regular exp. Recursive')
    search_parser.add_argument('pattern', type=str, help='Pattern to find')
    search_parser.add_argument('-d', '--dir', default=os.getcwd(), help='Directory where to search')
    search_parser.set_defaults(func=functional.re_search)
    # Date file
    date_parser = subparsers.add_parser('date', help='Takes dir/file and puts date of creation in every file names')
    date_parser.add_argument('dir', type=str, help='Either dir or file')
    date_parser.add_argument('-r', '--recursive', action='store_true')
    date_parser.set_defaults(func=functional.date_file)
    # Analyze
    analyze_parser = subparsers.add_parser('analyze', help='Takes dir and analyzes every file and dir size. Returns size of dir')
    analyze_parser.add_argument('dir', type=str, help='Dir to analyze')
    analyze_parser.set_defaults(func=functional.analyze)

    return parser.parse_args(args_list)


def main(args_list=None):
    """
    Парсит аргументы, и после исполняет команду
    """
    args = parse_args(args_list)

    commands = {
        'copy': functional.copy_file,
        'delete': functional.delete_file,
        'count': functional.count_files,
        'search': functional.re_search,
        'date': functional.date_file,
        'analyze': functional.analyze
    }

    if args.command == 'search':
        commands[args.command](args.pattern)
    elif args.command == 'date' and args.recursive:
        commands[args.command](args.dir, args.recursive)
    else:
        commands[args.command](args.dir)


if __name__ == '__main__':
    main()
