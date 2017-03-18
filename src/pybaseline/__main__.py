"""Main entry point."""
from argparse import ArgumentParser
import sys
from .example_module import example_function


PARSER = ArgumentParser(description='Example Python')
PARSER.add_argument('--expected_result',
                    action='store',
                    type=int,
                    default=7,
                    help='The expected result (default: %(default)s)')


def main():
    """Main entry point."""
    parsed = PARSER.parse_args(sys.argv[1:])
    return example_function(parsed.expected_result)


if __name__ == '__main__':
    print main()
