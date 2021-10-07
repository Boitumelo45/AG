import unittest
import os
import re


class TestUser(unittest.TestCase):
    user_text_file = os.path.join(os.path.split(os.path.abspath(__file__))[0], "data", "user.txt")

    def test_file_extension(self):
        self.assertEqual('user.txt', os.path.split(TestUser.user_text_file)[-1])

    def test_file_exists(self):
        self.assertTrue(os.path.isfile(TestUser.user_text_file), f"{TestUser.user_text_file} does not exists")

    def test_file_readable(self):
        self.assertTrue(os.access(TestUser.user_text_file, os.R_OK), f"{TestUser.user_text_file} is not readable")

    def test_file_size(self):
        self.assertNotEqual(0, os.stat(TestUser.user_text_file).st_size, "File is empty")

    def test_delimiters_name_format(self):
        with open(TestUser.user_text_file, 'r') as data_user_txt:
            rows = data_user_txt.readlines()
            for row in rows:
                self.assertIn("follows", row, "Wrong delimiter found instead of follows")
                get = row.split("follows")
                all_names = [get[0].strip()] + [usr.strip() for usr in get[-1].split(",")]  # flatten all users
                for name in all_names:
                    self.assertTrue(bool(re.findall("^[A-Z]{1}", name)), "check name format {}".format(name))

    def test_delimiter(self):
        with open(TestUser.user_text_file, 'r') as data_user_txt:
            rows = data_user_txt.readlines()
            for row in rows:
                get = row.split("follows")
                _delimiters = [t.strip() for t in re.findall(r"\W+", get[-1])]
                chars = [chr(t) for t in list(range(33, 44)) + list(range(47, 48)) + list(range(58, 65))]
                if set(_delimiters) & set(chars):
                    raise Exception(f"Found illegal delimiters {get[-1]}")


if __name__ == '__main__':
    unittest.main()
