import os
import shutil
import tempfile
from validate_user_base import parse_args, is_record_correct, validate_registration, csv_existence_checker, \
    get_csv_content, is_registration_inside_csv, csv_entry, execute_script

BASE_NAME = 'temporary_database.csv'


def test_parse_args():
    # Test default:
    assert parse_args(['-e', 'mail@gmail.com', '-p', 'pass']) == {
        'email': 'mail@gmail.com', 'password': 'pass', 'telephone': '000-000-000', 'zip_code': '00-000'}
    # Test various inputs:
    assert parse_args(['-e', 'mail@gmail.com', '-p', 'pass', '-t', '123-456-789', '-z', '90-210']) == {
        'email': 'mail@gmail.com', 'password': 'pass', 'telephone': '123-456-789', 'zip_code': '90-210'}
    # Test missing email:
    assert parse_args(['-p', 'OnlyPassword1']) == {}
    # Test missing password:
    assert parse_args(['-e', 'mail@gmail.com']) == {}


def test_is_record_correct():
    assert is_record_correct('email', '$@gmail.com') is False
    assert is_record_correct('email', 'user@$.com') is False
    assert is_record_correct('email', 'user@gmail.com') is True

    assert is_record_correct('password', 'Admin11') is False  # too short
    assert is_record_correct('password', 'password') is False  # only small letters
    assert is_record_correct('password', 'password1') is False  # only small letters and digits
    assert is_record_correct('password', 'Password1') is True  # strong password
    assert is_record_correct('password', 'Password11') is True  # also strong password (9 characters)

    assert is_record_correct('zip_code', '997-') is False
    assert is_record_correct('zip_code', '-666') is False
    assert is_record_correct('zip_code', '90*210') is False
    assert is_record_correct('zip_code', '90-210') is True

    assert is_record_correct('telephone', '12345678') is False
    assert is_record_correct('telephone', '123456789') is True
    assert is_record_correct('telephone', '1234 567 89') is False
    assert is_record_correct('telephone', '123 456 789') is True
    assert is_record_correct('telephone', '1234-56789') is False
    assert is_record_correct('telephone', '123-456-789') is True
    assert is_record_correct('telephone', '+48 123456789') is True
    assert is_record_correct('telephone', '+48 123 456 789') is True
    assert is_record_correct('telephone', '+48 123-456-789') is True


def test_validate_registration():
    assert validate_registration({'email': '!@gmail.com', 'password': 'Password1', 'telephone': '123-456-789',
                                  'zip_code': '90-210'}) is False  # wrong email
    assert validate_registration({'email': 'mail@gmail.com', 'password': 'pass', 'telephone': '123-456-789',
                                  'zip_code': '90-210'}) is False  # weak password
    assert validate_registration({'email': 'mail@gmail.com', 'password': 'Password1', 'telephone': '1234-56-789',
                                  'zip_code': '90-210'}) is False  # wrong telephone format
    assert validate_registration({'email': 'mail@gmail.com', 'password': 'Password1', 'telephone': '123-456-789',
                                  'zip_code': '902-10'}) is False  # wrong zip code
    assert validate_registration({'email': 'mail@gmail.com', 'password': 'Password1', 'telephone': '123-456-789',
                                  'zip_code': '90-210'}) is True


class TestCsv:
    def setup_method(self):
        self.test_dir = tempfile.mkdtemp()
        os.chdir(self.test_dir)
        csv_existence_checker(BASE_NAME)
        csv_entry(BASE_NAME, {'email': 'tomo@gmail.com', 'password': 'Password1', 'telephone': '123-456-789',
                              'zip_code': '90-210'})

    def teardown_method(self):
        shutil.rmtree(self.test_dir, ignore_errors=True)

    def test_csv_existence_checker(self):
        additional_base = 'different_base.csv'
        assert (additional_base in os.listdir(self.test_dir)) is False
        csv_existence_checker(additional_base)
        assert (additional_base in os.listdir(self.test_dir)) is True
        assert get_csv_content(additional_base) == [['email', 'password', 'telephone', 'zip-code']]

    def test_get_csv_content(self):
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210']]

    def test_is_registration_inside_csv(self):
        # email already registered
        assert is_registration_inside_csv(BASE_NAME, {'email': 'tomo@gmail.com', 'password': 'Password1',
                                                      'telephone': '123-456-789', 'zip_code': '90-210'}) is True
        # email already registered, even if pass, tel and zip are different
        assert is_registration_inside_csv(BASE_NAME, {'email': 'tomo@gmail.com', 'password': 'pass_is_different',
                                                      'telephone': '888-888-888', 'zip_code': '88-888'}) is True
        # email is new
        assert is_registration_inside_csv(BASE_NAME, {'email': 'not_existing_mail', 'password': 'Password1',
                                                      'telephone': '123-456-789', 'zip_code': '90-210'}) is False

    def test_csv_entry(self):
        csv_entry(BASE_NAME,
                  {'email': 'new_mail@gmail.com', 'password': 'NewPassword1', 'telephone': '987-654-321',
                   'zip_code': '58-100'})
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['new_mail@gmail.com', 'NewPassword1', '987-654-321', '58-100']]

    def test_execute_script(self):
        # first correct entry (default)
        execute_script(['-e', 'name.surname@wp.pl', '-p', 'Difficult69'], BASE_NAME)
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['name.surname@wp.pl', 'Difficult69', '000-000-000', '00-000']]
        # wrong entry - missing email
        execute_script(['-p', 'Difficult69', '-t', '224 444 444', '-z', '99-100'], BASE_NAME)
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['name.surname@wp.pl', 'Difficult69', '000-000-000', '00-000']]
        # wrong entry - missing password
        execute_script(['-e', 'name@wp.pl', '-t', '224 444 444', '-z', '99-100'], BASE_NAME)
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['name.surname@wp.pl', 'Difficult69', '000-000-000', '00-000']]

        # wrong entry - weak password
        execute_script(['-e', 'name@wp.pl', '-p', 'weak_password', '-t', '224 444 444', '-z', '99-100'], BASE_NAME)
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['name.surname@wp.pl', 'Difficult69', '000-000-000', '00-000']]
        # second correct entry
        execute_script(['-e', 'work@wp.pl', '-p', 'better_Password5', '-t', '224 444 444', '-z', '99-100'], BASE_NAME)
        assert get_csv_content(BASE_NAME) == [['email', 'password', 'telephone', 'zip-code'],
                                              ['tomo@gmail.com', 'Password1', '123-456-789', '90-210'],
                                              ['name.surname@wp.pl', 'Difficult69', '000-000-000', '00-000'],
                                              ['work@wp.pl', 'better_Password5', '224 444 444', '99-100']]


