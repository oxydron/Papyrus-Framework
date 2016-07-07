from time import time

class Token(object):
	"""
	Class that represents a hashble token.
	"""
	def __init__(self, strtoken):
		super(Token, self).__init__()
		self.hashcode = hash(strtoken)
		self.strtoken = strtoken

	def __eq__(self, other):
		return self.hashcode == other.hashcode

	def __repr__(self):
		return self.strtoken

def tokenizer(word, tokensize=2, lowercase=True, start_symbol='$', end_symbol='@'):
	"""
	Function that tokenize a word in a set of tokens.
	"""
	# sum up the start and end symbol on the word
	word = start_symbol+word+end_symbol
	# do lowercase?
	if lowercase:
		word = word.lower()

	assert(tokensize>0)
	assert(type(tokensize) is int)
	output = list()
	for i in range(len(word)-tokensize+1):
		output.append(Token(word[i:i+tokensize]))

	return tuple(output)

def main():
	for i in range(100000):
		tokenizer('Ben Hur')

if __name__ == '__main__':
	t = time()
	main()
	print(time()-t)