import argparse
import csv
import logging
import os
import re
import sys

EMAIL_REGEX = re.compile(r'''(
    [a-zA-Z0-9._%+-]+  
    @
    [a-zA-Z0-9.-]+  
    .
    \.[a-zA-Z]{2,4}
    )''', re.VERBOSE)
PASSWORD_REGEX = re.compile(r'''
        (?=.*[A-Z]) # positive look ahead assertions
        (?=.*[0-9])
        (?=.*[a-z])
        .{8}
        ''', re.VERBOSE)
TELEPHONE_REGEX = re.compile(r'''(
    (\+\d{2}\s)?
    (
    \d{3}
    [\s-]?
    \d{3}
    [\s-]?
    \d{3}
    )
    )''', re.VERBOSE)
ZIP_CODE_REGEX = re.compile(r'\d\d-\d\d\d')
REGEX_DATABASE = {'email': EMAIL_REGEX, 'password': PASSWORD_REGEX, 'telephone': TELEPHONE_REGEX,
                  'zip_code': ZIP_CODE_REGEX}


def parse_args(args):
    parser = argparse.ArgumentParser('Collect database of mail, pass, tel and zip inside csv.')
    parser.add_argument('-e', action='store', dest='email', help='Email of user. This is unique filed for database.')
    parser.add_argument('-p', action='store', dest='password', help='Password of user.')
    parser.add_argument('-t', action='store', dest='telephone', default='000-000-000', help='Telephone of user.')
    parser.add_argument('-z', action='store', dest='zip_code', default='00-000', help='Zip code of user.')
    parameters = parser.parse_args(args)
    if not parameters.email or not parameters.password:
        return {}
    else:
        return vars(parameters)


def is_record_correct(record_type, record):
    return re.match(REGEX_DATABASE[record_type], record) is not None


def validate_registration(registration):
    for position in registration:
        if not is_record_correct(position, registration[position]):
            return False
    return True


def csv_existence_checker(csv_file_name):
    if not os.path.isfile(csv_file_name):
        with open(csv_file_name, 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(['email', 'password', 'telephone', 'zip-code'])  # columns names


def get_csv_content(csv_filename):
    csv_content = []
    with open(csv_filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            csv_content.append(row)
    return csv_content


def is_registration_inside_csv(csv_file_name, registration):
    csv_content = get_csv_content(csv_file_name)
    line_count = 0
    for row in csv_content:
        if line_count == 0:
            pass  # columns names
        else:
            if row[0] == registration['email']:
                logging.log(logging.WARNING, "This registration is already inside file.")
                return True
        line_count += 1
    logging.log(logging.INFO, "This registration is new inside CSV file.")
    return False


def csv_entry(csv_file_name, registration):
    with open(csv_file_name, 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([registration['email'], registration['password'], registration['telephone'],
                         registration['zip_code']])


def execute_script(args, csv_file_name):
    csv_existence_checker(csv_file_name)
    user_input = parse_args(args)
    if not user_input:
        logging.log(logging.WARNING, "Received parameters are missing")
        return
    logging.log(logging.INFO, "Received following registration:")
    logging.log(logging.INFO, user_input)
    if not validate_registration(user_input):
        logging.log(logging.WARNING, "This registration contains wrong record.")
        return
    logging.log(logging.INFO, "This registration is correctly validated by regular expressions.")
    if is_registration_inside_csv(csv_file_name, user_input):
        logging.log(logging.INFO, "Entry already exists.")
    csv_entry(csv_file_name, user_input)


if __name__ == '__main__':
    logging.basicConfig(filename='validated_registration_log.txt', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    execute_script(sys.argv[1:], 'database.csv')
