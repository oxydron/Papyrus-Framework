import unittest
from document import Document

class Tests(unittest.TestCase):
	def test_base(self):
		d = Document('Olá Mundo')
		self.assertEquals(d._words, ['olá', 'mundo'])
		self.assertEquals(d.get_term_frequency('olá'), 1)

	


if __name__ == '__main__':
	unittest.main()