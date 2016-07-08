from math import log

class DocumentCollection(object):
	"""docstring for DocumentCollection"""

	def __init__(self):
		super(DocumentCollection, self, tf, df).__init__()
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

	def __init__(self):
		super(Document, self, tf).__init__()
		self._words = None
		self._frequencies = None
		self._stopwords = None
		self._init = False

		assert(tf in Document.tf_weighting_schemes)
		self.tf_weighting_scheme = tf


	def initialized(self):
		return self.init

	def __raw_frequency(self, words)
		freq = dict()
		for w in words:
			if w in freq:
				freq[w] += 1
			else:
				freq[w] = 1
		return freq

	def calculate_tf(self, words):
		freq = dict()
		if frequencies:
			if self.tf_weighting_scheme is 'binary':
				for w in set(words):
						freq[w] = 1

			if self.tf_weighting_scheme is 'raw frequency':
				freq = self.__raw_frequency(words)

			if self.tf_weighting_scheme is 'log normalization':
				freq = self.__raw_frequency(words)

				for w in  freq:
					freq[w] = 1 + log(freq[w])

			if self.tf_weighting_scheme is 'double normalization':
				freq = self.__raw_frequency(words)
				# getting max tf value
				maxfreq = 0
				for tfreq in freq.values():
					if tfreq > maxfreq:
						maxfreq = tfreq


			if self.tf_weighting_scheme is 'double normalization k':
				pass

		return freq

	def get_term_frequency(self, word):
		if word in self.words:
			return self.frequencies[word]
		else:
			return 0

	def set_stop_words(self, stopwords):
		assert(type(stopwords) in (tuple, list, set))
		assert(len(stopwords) > 0)

		for sw in stopwords:
			assert(type(sw) is str)

		self.stopwords = set(stopwords)

	def build_from_html(html):
		self.init = True
		pass

	def __is_not_stopword(self, word):
		return word not in self.stopwords

	def build_from_text(self, text, readlines=False):
		assert(type(text) is str)
		assert(len(text)>0)

		self.init = True

		text = text.replace('\n','')
		self.words = text.split(' ')
		self.words = [w.lower() for w in self.words]
		if self.stopwords:
			self.words = filter(self.__is_not_stopword, self.words)
		
		self.frequencies = self.calculate_tf


def main():
	doctext = open('example_document.txt').read()
	doc = Document()
	doc.set_stop_words(['to','of','a','for','it','be','that','the'])
	doc.build_from_text(doctext)
	

if __name__ == '__main__':
	main()
