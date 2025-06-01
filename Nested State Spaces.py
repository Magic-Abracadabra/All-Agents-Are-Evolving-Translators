class s0():
	def __init__(self, s):
		self.s = s
		self.l = 0	

class w():
	def __init__(self, l, W0, T=None, G=[]):
		if type(G)==list and type(l)==int and l>=0 and l==W0.l+1:
			pass
		else:
			raise ValueError('at least one of them wrong: level l; representative element W0; tag T; generation rule G')
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
	def __init__(self, l, words=None):
		if all(list(map(lambda x: x[0]==l and type(x)==tuple and len(x)==3, words))) and type(words)==list:
			self.s = words
		elif words==None:
			self.s = []
		else:
			raise ValueError(f'Cannot form a list of words at level {l}!')
		self.l = l
	def __eq__(self, target):
		return self.s==target.s
	def insert(self, word, position=None):
		if all([self.l==word[0], type(word)==tuple, len(word)==3]):
			if position==None:
				self.s.append(word)
			else:
				self.s.insert(position, word)
		else:
			raise ValueError('Level Error or Position Error!')

class nss():
	def __init__(self, pairs=[]):
		self.ids = []
		self.words = []
		try:
			for id, word in pairs:
				assert all([type(id)==tuple, len(id)==3, type(id[0])==int, type(word)==w, word.l==id[0]])
				assert id not in self.ids; assert word not in self.words
				self.ids.append(id); self.words.append(word)
		except:
			raise TypeError('Not pairwise (id triple, word) or Repetitive!')
	def __call__(self, target):
		if type(target)==tuple:
			return self.words[self.ids.index(target)]
		elif type(target)==w:
			return self.ids[self.words.index(target)]
		else:
			raise TypeError
	def insert(self, id, word):
		assert all([type(id)==tuple, len(id)==3, type(id[0])==int, type(word)==w, word.l==id[0]])
		assert id not in self.ids; assert word not in self.words
		self.ids.append(id); self.words.append(word)
