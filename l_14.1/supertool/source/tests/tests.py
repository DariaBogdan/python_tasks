import io
import os
import unittest
import unittest.mock

import supertool.similar

DIRECTORY = 'supertool_tmp'


class TestSupertool(unittest.TestCase):
    """Creating temporary folder in setUp, filling it with files,
    working, then deleting temporary folder with tearDown.
    """
    def setUp(self):
        if not os.path.exists(DIRECTORY):
            os.makedirs(DIRECTORY)
        with open(os.path.join(DIRECTORY, '1'), 'w') as f:
            f.write('hello')
        with open(os.path.join(DIRECTORY, '2'), 'w') as f:
            f.write('hello')
        with open(os.path.join(DIRECTORY, '3'), 'w') as f:
            f.write('hello')
        with open(os.path.join(DIRECTORY, '4'), 'w') as f:
            f.write('hello!')
        with open(os.path.join(DIRECTORY, '5'), 'w') as f:
            f.write('hello!')
        with open(os.path.join(DIRECTORY, '6'), 'w') as f:
            f.write('hello!!!')

    def tearDown(self):
        for root, directories, file_paths in os.walk(DIRECTORY):
            print(root)
            for file_path in file_paths:
                os.remove(os.path.join(root, file_path))
            for directory in directories:
                os.rmdir(os.path.join(root, directory))
            os.rmdir(root)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_assert_stdout(self, mock_stdout):
        supertool.similar.work(DIRECTORY)

        expected_output = "This 2 files are the same:\n['supertool_tmp/4', 'supertool_tmp/5']\n" \
                          "This 3 files are the same:\n['supertool_tmp/3', 'supertool_tmp/1', 'supertool_tmp/2']\n"

        self.assertEqual(mock_stdout.getvalue(), expected_output)