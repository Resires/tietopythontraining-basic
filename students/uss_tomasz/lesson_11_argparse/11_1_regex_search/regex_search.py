# Usage:
# python regex_search.py -r \d{3}
# python regex_search.py -r \d{3} -p First_lvl_dir\Second_lvl_dir
import argparse
import os
import re
import sys


def parse_args(args):
    parser = argparse.ArgumentParser('Searching for a specified regex inside all text files in current directory.')
    parser.add_argument('-r', action='store', dest='regex', default=r'\d{3}', help='Store a regular expression.')
    parser.add_argument('-p', action='store', dest='path', default='.', help='Store a path to the dir with files.')
    return parser.parse_args(args).regex, parser.parse_args(args).path


def get_file_names_list(directory_path):
    return [f for f in os.listdir(directory_path) if f.endswith('.txt')]


def find_regex_in_txt_files(regex, directory_path):
    results = {}
    for text_file_name in get_file_names_list(directory_path):
        with open(os.path.join(directory_path, text_file_name), 'r') as text_file:
            text = text_file.read()
        results[text_file_name] = re.findall(regex, text)
    return results


def execute_script(args):
    user_regex, files_localisation = parse_args(args)
    regex_findings = find_regex_in_txt_files(user_regex, files_localisation)
    message = ''
    for file_name in regex_findings:
        for regex_finding in regex_findings[file_name]:
            message += 'In file named "{}" there were following occurrence: {} \n'.format(file_name, regex_finding)
    return message


if __name__ == '__main__':
    print(execute_script(sys.argv[1:]))
