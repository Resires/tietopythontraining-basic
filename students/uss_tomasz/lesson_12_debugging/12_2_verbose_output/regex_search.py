import argparse
import logging
import os
import re
import sys


def parse_args(args):
    parser = argparse.ArgumentParser('Searching for a specified regex inside all text files in current directory.')
    parser.add_argument('-r', action='store', dest='regex', default=r'\d{3}', help='Store a regular expression.')
    parser.add_argument('-p', action='store', dest='path', default='.', help='Store a path to the dir with files.')
    parser.add_argument('-v', action='store', dest='verbosity', default=2, type=int, choices=range(3),
                        help='Set the level of verbosity. 0=none, 1=critical & error, 2=full')
    parser.add_argument('-n', action='store', dest='log_file_name', default='regex_search_log.txt', type=str,
                        help='Change the name of log file')
    received_args = parser.parse_args(args)
    return received_args.regex, received_args.path, received_args.verbosity, received_args.log_file_name


def verbosity_deactivation(verbosity_lvl):
    if verbosity_lvl == 0:
        logging.disable(logging.CRITICAL)
    elif verbosity_lvl == 1:
        logging.disable(logging.WARNING)
    logging.log(logging.DEBUG, 'Following file has a visible DEBUG messages')
    logging.log(logging.INFO, 'Following file has a visible INFO messages')
    logging.log(logging.WARNING, 'Following file has a visible WARNING messages')
    logging.log(logging.ERROR, 'Following file has a visible ERROR messages')
    logging.log(logging.CRITICAL, 'Following file has a visible CRITICAL messages')


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
    # Loop with handlers is needed, because logging was not creating log file in temp folders:
    for handler in logging.root.handlers[:]:
        logging.root.removeHandler(handler)

    user_regex, files_localisation, user_verbosity_lvl, user_log_file_name = parse_args(args)
    if not os.path.exists(files_localisation):
        os.mkdir(files_localisation)
    logging.basicConfig(filename=os.path.join(files_localisation, user_log_file_name), level=logging.DEBUG,
                        format='%(levelname)s - %(message)s')
    verbosity_deactivation(user_verbosity_lvl)
    logging.log(logging.INFO, "Regex to search: ")
    logging.log(logging.INFO, user_regex)
    message = ''
    text_file_names = get_file_names_list(files_localisation)
    if len(text_file_names) == 0:
        logging.log(logging.ERROR, 'There are no text files')
    else:
        logging.log(logging.INFO, 'In current directory there are following text files: {}'.format(text_file_names))
        regex_findings = find_regex_in_txt_files(user_regex, files_localisation)
        for file_name in regex_findings:
            for regex_finding in regex_findings[file_name]:
                message += 'In file named "{}" there were following occurrence: {} \n'.format(file_name, regex_finding)
    return message


if __name__ == '__main__':
    print(execute_script(sys.argv[1:]))
