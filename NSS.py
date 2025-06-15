class s0():
	def __init__(self, s):
		self.s = s
		self.l = 0	

class w():
	def __init__(self, l, W0, T=None, G=[]):
		if type(G)==list and type(l)==int and l>=0 and l==W0.l+1:
			pass
		else:
			raise ValueError('At least one of them wrong: level l; representative element W0; tag T; generation rule G')
		self.l = l
		self.W0 = W0
		self.T = T
		self.G = G
		self.W = []
		for item in G:
			self.W.append(item)
	def __eq__(self, target):
		return all([self.l==target.l, self.W0==target.W0, self.T==target.T, self.G==target.G, self.W==target.W])

class s():
	def __init__(self, l, words):
		if type(words)==list and all(list(map(lambda x: x[0]==l and type(x)==list and len(x)==3, words))):
			self.s = words
		else:
			raise ValueError(f'Cannot form a list of words at level {l}!')
		self.l = l
	def __eq__(self, target):
		return self.s==target.s

class nss():
	def __init__(self, pairs=[]):
		self.ids = []
		self.words = []
		try:
			for ID, word in pairs:
				assert all([type(ID)==list, len(ID)==3, type(ID[0])==int, type(word)==w, word.l==ID[0]])
				assert ID not in self.ids; assert word not in self.words
				self.ids.append(ID); self.words.append(word)
		except:
			raise TypeError('Not pairwise (ID triple, word) or Repetitive!')
	def __call__(self, target):
		if type(target)==list:
			return self.words[self.ids.index(target)]
		elif type(target)==w:
			return self.ids[self.words.index(target)]
		else:
			raise TypeError
	def insert(self, word):
		assert type(word)==w
		ID = [word.l, word.T, word.W0.s]
		assert ID not in self.ids; assert word not in self.words
		self.ids.append(ID); self.words.append(word)
	def remove(self, word):
		assert type(word)==w
		ID = self(word)
		assert ID in self.ids; assert word in self.words
		self.ids.remove(ID); self.words.remove(word)
	def receptor_grows(self, l):
		receptor = []
		for coordinate in self.ids:
			if coordinate[0]==l:
				word = self(coordinate)
				for probe in list(map(lambda x: x.s, word.W)):
					receptor.append([probe, coordinate])
		receptor.sort(key=lambda x: len(x[0]), reverse=True)
		return receptor