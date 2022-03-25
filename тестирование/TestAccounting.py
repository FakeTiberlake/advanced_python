import unittest
from accounting import get_all_docs, add_new_doc, delete_doc

class TestAccounting(unittest.TestCase):

    def SetUp(self):
        print('Testing secretary functions...')

    def test_get_all_docs(self):
        self.assertEqual(accounting.get_all_docs('2207 876234'), 'invoice "11-2" "Василий Гупкин"')

    def test_remove_doc_from_shelf(self):
        accounting.remove_doc_from_shelf('10006')
        self.assertEqual(accounting.directories['2'], [])

    @patch('builtins.input')
    def test_delete_doc(self, user_input):
        user_input.side_effect = ['11-2']
        self.assertEqual(accounting.delete_doc(), ('11-2', True))

    def tearDown(self):
        print('Testing complete!')


# if __name__ == '__main__':
#     unittest.main()
