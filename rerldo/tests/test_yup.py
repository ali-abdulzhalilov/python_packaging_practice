from unittest import TestCase

import rerldo

class TestYup(TestCase):
	def test_is_string(self):
		s = rerldo.yup()
		self.assertTrue(isinstance(s, str))