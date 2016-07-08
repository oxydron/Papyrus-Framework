from math import log

class DocumentCollection(object):
	"""docstring for DocumentCollection"""

	def __init__(self, tf, df):
		super(DocumentCollection, self).__init__()
		self.documents = list()
		self.tf_weighting_scheme = tf
		self.df_weighting_scheme = df

	def add_document(self, doc):
		assert(type(doc) is Document)
		assert(document.initialized())

class Document(object):
	"""docstring for Document"""
	tf_weighting_schemes = ('binary','raw frequency','log normalization',
		'double normalization', 'double normalization k')

	def __init__(self, tf):
		super(Document, self).__init__()
		self._words = None
		self._frequencies = None
		self._stopwords = None
		self._init = False

		assert(tf in Document.tf_weighting_schemes)
		self.tf_weighting_scheme = tf


	def initialized(self):
		return self.init

	def _raw_frequency(self, words):
		freq = dict()
		for w in words:
			if w in freq:
				freq[w] += 1
			else:
				freq[w] = 1
		return freq

	def _calculate_tf(self, words):
		freq = dict()
		
		if self.tf_weighting_scheme == 'binary':
			for w in set(words):
					freq[w] = 1

		if self.tf_weighting_scheme == 'raw frequency':
			freq = self._raw_frequency(words)			

		if self.tf_weighting_scheme == 'log normalization':

			freq = self._raw_frequency(words)

			for w in  freq:
				freq[w] = 1 + log(freq[w])

		if self.tf_weighting_scheme == 'double normalization':
			freq = self._raw_frequency(words)
			# getting max tf value
			maxfreq = 0
			for tfreq in freq.values():
				if tfreq > maxfreq:
					maxfreq = tfreq

		if self.tf_weighting_scheme == 'double normalization k':
			pass

		return freq

	def get_term_frequency(self, word):
		"""
		Get the term frequency on the document. If a word doesn't belong to this 
		document, it returns 0.
		"""
		word = word.lower()
		if word in self._words:
			return self._frequencies[word]
		else:
			return 0

	def set_cleaning_str(self, list_str):
		"""
		Set which substrings must be removed for every word. Common options are 
		dot, commas, new line string '\n'
		"""
		# TODO implementar

	def set_stop_words(self, stopwords):
		"""
		Set the stop words for this document.
		"""

		assert(type(stopwords) in (tuple, list, set))
		assert(len(stopwords) > 0)

		for sw in stopwords:
			assert(type(sw) is str)

		self.stopwords = set(stopwords)

	def __is_not_stopword(self, word):
		return word not in self.stopwords

	def build_from_filename(self, filename):
		"""
		Build a document from a filename
		"""
		self.build_from_str(open(filename).read())

	def build_from_str(self, text, readlines=False):
		"""
		Create a document from a string.
		"""
		assert(type(text) is str)
		assert(len(text)>0)

		self.init = True

		text = text.replace('\n','')
		text = text.replace('.','')
		text = text.replace(',','')

		words = text.split(' ')
		words = [w.lower() for w in words]
		if self.stopwords:
			words = list(filter(self.__is_not_stopword, words))
		
		self._frequencies = self._calculate_tf(words)
		self._words = words

def main():
	doctext = open('example_document.txt').read()
	doc = Document('log normalization')
	doc.set_stop_words(['to','of','a','for','it','be','that','the'])
	doc.build_from_str(doctext)
	print(doc.get_term_frequency('tf-idf'))

if __name__ == '__main__':
	main()
