# Usage: python regex_search.py -r \d{3}
import argparse
import os
import re
import sys


def parse_args(args):
    parser = argparse.ArgumentParser('Searching for a specified regex inside all text files in current directory.')
    parser.add_argument('-r', action='store', dest='regex', default=r'\d{3}', help='Store a regular expression.')
    return parser.parse_args(args).regex


def get_file_names_list():
    return [f for f in os.listdir(os.curdir) if os.path.isfile(f) and f.endswith('.txt')]


def find_regex_in_txt_files(regex):
    results = {}
    for text_file_name in get_file_names_list():
        with open(text_file_name, 'r') as text_file:
            text = text_file.read()
        results[text_file_name] = re.findall(regex, text)
    return results


if __name__ == '__main__':
    with open('text1.txt', 'w') as file:
        file.write('Write a program that opens all .txt files in a folder 123')
    with open('text2.txt', 'w') as file:
        file.write('Program searches for any line that matches a user-supplied regular expression 456 789')
    with open('text3.txt', 'w') as file:
        file.write('666 The results should be printed to the screen 997')
    user_regex = parse_args(sys.argv[1:])
    regex_findings = find_regex_in_txt_files(user_regex)
    for file_name in regex_findings:
        for regex_finding in regex_findings[file_name]:
            print('In file named "{}" there were following occurrence: {}'.format(file_name, regex_finding))
    os.remove('text1.txt')
    os.remove('text2.txt')
    os.remove('text3.txt')
