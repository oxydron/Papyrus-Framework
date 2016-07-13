from math import log

class DocumentCollection(object):
	"""docstring for DocumentCollection"""
	tf_weighting_schemes = ('binary','raw frequency','log normalization',
		'double normalization', 'double normalization k')

	df_weighting_schemes = ()

	def __init__(self, tf, df):
		super(DocumentCollection, self).__init__()
		self._documents = list()
		self._tf_weighting_scheme = tf
		self._df_weighting_scheme = df

	def add_document(self, doc):
		assert(type(doc) is Document)
		assert(document.initialized())
		self.documents

	def build_from_filenames(self, filenames):
		pass
		# TODO implementar

class Document(object):
	"""
	Class definition for a text document. You may inform
	which term frequency weighting scheme should be used, the standard is
	log normalization. 

	Possible weighting schemes: 'binary','raw frequency','log normalization',
	'double normalization', 'double normalization k'
	"""
	tf_weighting_schemes = {'binary','raw frequency','log normalization',
		'double normalization', 'double normalization k'}

	def __init__(self, text=''):
		super(Document, self).__init__()
		self._words = None
		self._frequencies = None
		self._stopwords = None
		self._text = text
		self.tf_weighting_scheme = 'log normalization'
		if text:
			self._init = True
		else:
			self._init = False

	def is_initialized(self):
		"""
		Return true if this object is initialized or false otherwise.
		"""
		return self._init

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

	def set_stop_words_file(self, filename, sep=' '):
		stopwords = open(filename).read().split(sep)
		self.set_stop_words(stopwords)


	def set_stop_words(self, stopwords):
		"""
		Set the stop words for this document.
		"""

		assert(type(stopwords) in (tuple, list, set))
		assert(len(stopwords) > 0)

		for sw in stopwords:
			assert(type(sw) is str)

		self._stopwords = set(stopwords)

	def __is_not_stopword(self, word):
		return word not in self.stopwords

	def create_from_filename(self, filename):
		"""
		Build a document from a filename
		"""
		self.create_from_str(open(filename).read())

	def create_from_str(self, text, readlines=False):
		"""
		Create a document from a string.
		"""
		assert(type(text) is str)
		assert(len(text)>0)
		self._text = text
		self._init = False

	def init(self):
		"""
		Initialize the document with the configuration given.
		"""
		# TODO usar dados do método
		text = self._text
		self._text = None

		self._words = text.replace('\n','')
		self._words = text.replace('.','')
		self._words = text.replace(',','')

		self._words = text.split(' ')
		self._words = [w.lower() for w in words]
		if self._stopwords:
			self._words = list(filter(self.__is_not_stopword, words))
		
		self._frequencies = self._calculate_tf(self._words)
		self._init = True


def main():
	doc = Document()
	doc.create_from_filename('example_document.txt')
	doc.set_stop_words(['to','of','a','for','it','be','that','the'])
	doc.init()
	

	#doccol = DocumentCollection()
	


if __name__ == '__main__':
	main()
