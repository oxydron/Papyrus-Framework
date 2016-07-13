
class WordPair(object):
	"""docstring for WordPair"""
	def __init__(self, u, v, value):
		super(WordPair, self).__init__()
		self.u = u
		self.v = v
		self.value = value

	def __repr__(self):
		return '(%s, %s, %0.2f)'%(self.u, self.v, self.value)

	def __lt__(self, other):
		return self.value < other.value

def partition(pairs):
	assert_pairs(pairs)
	mapper = dict()
	groups = dict()
	counter = 0

	for p in pairs:
		if p.u in mapper.keys():
			if p.v in mapper.keys():
				continue
			else:
				groups[mapper[p.u]].append(p.v)
				mapper[p.v] = mapper[p.u]
		else:
			if p.v in mapper.keys():
				groups[mapper[p.v]].append(p.u)
				mapper[p.u] = mapper[p.v]
				continue
			else:
				groups[counter] = [p.u, p.v]
				mapper[p.u] = counter
				mapper[p.v] = counter
				counter += 1
				
	return list(groups.values())

def center(pairs):
	assert_pairs(pairs)
	pairs = sorted(pairs, reverse=True)
	center = set()
	noncenter = set()
	clusters = dict()
	for p in pairs:
		if p.u != p.v:
			if (p.u not in center and p.u not in noncenter) and \
			(p.v not in center and p.v not in noncenter):
				center.add(p.u)
				noncenter.add(p.v)
				clusters[p.u] = [p.u, p.v]
			elif (p.u in center and p.v in center) or (p.u in noncenter and p.v in noncenter):
				continue
			elif p.v in center and p.u not in noncenter:
				noncenter.add(p.u)
				clusters[p.v].append(p.u)
			elif p.u in center and p.v not in noncenter:
				noncenter.add(p.v)
				clusters[p.u].append(p.v)
			else:
				continue

	return list(clusters.values())

def find_center(clusters, word):
	for center, cluster in cluster.items():
		if word in cluster:
			return center

def merge_center(pairs):
	assert_pairs(pairs)
	pairs = sorted(pairs, reverse=True)
	center = set()
	noncenter = set()
	clusters = dict()

	for p in pairs:
		if p.u != p.v:
			# both u and v are new, create a cluster with u as center
			if (p.u not in center and p.u not in noncenter) and\
			(p.v not in center and p.v not in noncenter):
				center.add(p.u)
				noncenter.add(p.v)
				clusters[p.u] = [p.u, p.v]

			# when u is a cluster center and v is too, merge them
			elif p.u in center and p.v in center:
				clusters[p.u] += clusters[p.v]
				del clusters[p.v]

			# when both are in clusters and none are center
			elif p.u in noncenter and v in noncenter:
				continue

			# when v is in a cluster and u is a center
			elif p.v in noncenter and p.u in center:
				v_center = find_center(p.v)
				clusters[p.u] += clusters[v_center]
				del clusters[v_center]

			elif p.u in noncenter and p.v in center:
				u_center = find_center(p.u)
				clusters[p.v] += clusters[u_center]
				del clusters[u_center]
			elif p.v in center:
				noncenter.add(p.u)
				clusters[p.v].append(p.u)
			elif p.u in center:
				noncenter.add(p.v)
				clusters[p.u].append(p.v)
			else:
				continue
	
	return list(clusters.values())	


def assert_pairs(pairs):
	"""
	Verify if pairs is a collection of Pair()
	"""
	assert type(pairs), type(list())
	assert type(pairs), type(tuple())
	
	for p in pairs:
		assert(type(p) is WordPair)

def main():
	pairs = list()
	pairs.append(WordPair('pedro','ben hur',0.2))
	pairs.append(WordPair('pedro','kika',0.9))
	pairs.append(WordPair('pedro','gabriel',0.3))
	pairs.append(WordPair('gabriel','pry',0.5))
	pairs.append(WordPair('carlos','joao',0.6))
	pairs.append(WordPair('jonatas','joao',0.1))
	#pairs=sorted(pairs, reverse=True)

	print(partition(pairs))
	print(center(pairs))
	print(merge_center(pairs))

if __name__ == '__main__':
	main()