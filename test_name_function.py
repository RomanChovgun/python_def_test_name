import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):

	def test_first_last_name(self):
		formatted_name = get_formatted_name('roman', 'chovgun')
		self.assertEqual(formatted_name, 'Roman Chovgun')

	def test_first_last_middle_name(self):
		formatted_name = get_formatted_name('roman', 'chovgun', 'olegovich')
		self.assertEqual(formatted_name, 'Roman Olegovich Chovgun')
		
unittest.main()