from math import log
from os import system

class DocumentCollection(object):
	"""
	Class that represents a collection of documents.

	Possible weighting schemes for term frequency:
	binary = 'bin'
	raw frequency = 'rf'
	log normalization = 'logn'
	double normalization = 'dn'
	double normalization k = 'dnk'

	Possible weighting schemes for inverse document frequency:
	unary = 'unary'
	inverse document frequency = 'idf'
	inverse document frequency smoth = 'idfs'
	inverse document frequency max = 'idfm'
	probabilistic inverse document frequency = 'pidf'
	"""
	tf_weighting_schemes = {'bin','rf','logn', 'dn', 'dnk'}
	idf_weighting_schemes = {'unary', 'idf', 'idfs', 'idfm', 'pidf'}

	def __init__(self, tf='rf', df='idf'):
		super(DocumentCollection, self).__init__()
		self._documents = list()
		self._tf_weighting_scheme = tf
		self._df_weighting_scheme = df
		self._inv_doc_freq = dict()

	def add_document(self, doc):
		assert(type(doc) is Document)
		self._documents.append(doc)
		self._calc_all_idf()

	def search(self, query):
		query = query.lower()
		query = query.split(' ')
		query = [token for token in query if token]

		# TODO 

	def _calc_idf(self, num_doc, n):

		if self._df_weighting_scheme == 'idf':
			return log(num_doc/n)

		elif self._df_weighting_scheme == 'idfs':
			return log(1+(num_doc/n))

		elif self._df_weighting_scheme == 'pidf':
			return log((num_doc-n)/n)

		# TODO implementar outros esquemas

	def _calc_all_idf(self):
		num_doc = len(self._documents)
		all_words = set()

		# TODO mudar para permitir adição e remoção de documentos

		# reseto contagens, refaço tudo
		self._inv_doc_freq = dict()

		# get all the words on the collection
		for doc in self._documents:
			for word in doc.words():
				all_words.add(word)

		# counting how much times a word appears in collection
		for word in all_words:
			n = 1
			for doc in self._documents:
				if word in doc:
					n += 1
			# now calc the idf using a weighting scheme
			self._inv_doc_freq[word] = self._calc_idf(num_doc, n)

		n = 1

class Document(object):
	"""
	Class definition for a text document. You may inform
	which term frequency weighting scheme should be used, the standard is
	log normalization. 

	Possible weighting schemes: 'bin'
	raw frequency = 'rf'
	log normalization = 'logn'
	double normalization = 'dn'
	double normalization k = 'dnk'
	"""
	tf_weighting_schemes = {'bin','rf','logn', 'dn', 'dnk'}

	def __init__(self, text, stopw=list(), cleanstr=list(), tf_scheme='log normalization', k=None):
		super(Document, self).__init__()
		self._stopwords = [w.lower() for w in stopw]
		self._cleaning_strs = cleanstr
		self._text = text
		self._hash = 0
		if self._text:
			self._hash = hash(self._text)
		self._tf_weighting_scheme = tf_scheme
		self._k = k  # for double normalization k
		self._words = None
		self._frequencies = None
		self.__init()

	def __hash__(self):
		return self._hash

	def __contains__(self, word):
		return word in self._words

	def words(self):
		return self._words

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
		
		if self._tf_weighting_scheme == 'binary':
			for w in set(words):
					freq[w] = 1

		if self._tf_weighting_scheme == 'raw frequency':
			freq = self._raw_frequency(words)			

		if self._tf_weighting_scheme == 'log normalization':

			freq = self._raw_frequency(words)

			for w in  freq:
				freq[w] = 1 + log(freq[w])

		if self._tf_weighting_scheme == 'double normalization':
			freq = self._raw_frequency(words)
			# getting max tf value
			maxfreq = 0
			for tfreq in freq.values():
				if tfreq > maxfreq:
					maxfreq = tfreq

		if self._tf_weighting_scheme == 'double normalization k':
			pass # TODO implementar

		return freq

	def frequencies(self):
		"""
		Return a dictionary with term frequencies.
		word -> frequency
		"""
		return self._frequencies

	def term_frequency(self, word):
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

	def __is_not_stopword(self, word):
		return word not in self._stopwords

	def __init(self):
		"""
		Initialize the document with the configuration given.
		"""
		# TODO usar dados do método
		text = self._text
		self._text = None

		# clean the strings with the provived cleaning strings
		for cleanstr in self._cleaning_strs:
			self._words = text.replace(cleanstr, '')
		
		self._words = text.split(' ')  # split the text on words
		self._words = [w.lower() for w in self._words]  # lowercase
		# get out stop words
		if self._stopwords:
			self._words = list(filter(self.__is_not_stopword, self._words))
		
		self._frequencies = self._calculate_tf(self._words)


def main():
	from os import listdir
	doc_dir = './docs/'
	docs = listdir(doc_dir)
	colec = DocumentCollection()
	stopwords=['to','of','a','for','it','be','that','the']

	for docname in docs:
		text = open(doc_dir+docname).read()
		doc = Document(text, stopwords)
		colec.add_document(doc)


	for i,j in colec._inv_doc_freq.items():
		print('%s: %s'%(i,j))

if __name__ == '__main__':
	main()
