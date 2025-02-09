from unittest.mock import patch
import functional
import pytest
import shlex
from fmanager import parse_args
"""
Тут расписаны тестовые кейсы(по одному на каждую команду), после чего тестируется парсинг аргументов для каждого случая
"""
@pytest.mark.parametrize(
    'command, expect_command, expect_dir, expect_pattern, expect_rec',
    [
        ('copy test', 'copy', 'test', None, False),
        ('delete test', 'delete', 'test', None, False),
        ('count test_dir', 'count', 'test_dir', None, False),
        ('search pattern -d dir', 'search', 'dir', 'pattern', False),
        ('date test_dir -r', 'date', 'test_dir', None, True),
        ('analyze test_dir', 'analyze', 'test_dir', None, False),
    ]
)
def test_parse(command, expect_command, expect_dir, expect_pattern, expect_rec):
    args = parse_args(shlex.split(command))

    assert args.command == expect_command
    assert args.dir == expect_dir if hasattr(args, 'dir') else True
    assert args.pattern == expect_pattern if hasattr(args, 'pattern') else True
    assert args.recursive == expect_rec if hasattr(args, 'recursive') else True
"""
А тут, при помощи мока, у нас тестируется вызов команд 
"""
@pytest.mark.parametrize(
    'command, expect_command, expect_dir, expect_pattern, expect_rec',
    [
        ('copy test', 'copy', 'test', None, False),
        ('delete test', 'delete', 'test', None, False),
        ('count test_dir', 'count', 'test_dir', None, False),
        ('search pattern -d dir', 'search', 'dir', 'pattern', False),
        ('date test_dir -r', 'date', 'test_dir', None, True),
        ('analyze test_dir', 'analyze', 'test_dir', None, False),
    ]
)
def test_command_exe(command, expect_command, expect_dir, expect_pattern, expect_rec):

    commands = {
        'copy': functional.copy_file,
        'delete': functional.delete_file,
        'count': functional.count_files,
        'search': functional.re_search,
        'date': functional.date_file,
        'analyze': functional.analyze
    }
    args = parse_args(shlex.split(command))
    with patch(f'functional.{commands[expect_command].__name__}') as mock_func:
        if args.command == 'search':
            mock_func(args.pattern)
        elif args.command == 'date' and args.recursive:
            mock_func(args.dir, args.recursive)
        else:
            mock_func(args.dir)
        mock_func.assert_called_once()