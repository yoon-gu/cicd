import unittest

class TestBasic(unittest.TestCase):
	def test_test(self):
		self.assertTrue(True)

	def test_import(self):
		import wolfgang as wg
		self.assertTrue(True)
