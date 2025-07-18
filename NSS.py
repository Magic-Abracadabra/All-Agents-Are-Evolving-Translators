class s0():
	def __init__(self, s):
		self.s = s
		self.l = 0
	def __eq__(self, target):
		return all([self.l==target.l, self.s==target.s])

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
		# To simplify, here we set:
		self.W = self.G
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
		return all([self.l==target.l, self.s==target.s])

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
	def levels(self):
		assert self.ids!=[] and self.words!=[]
		return sorted(self.ids, reverse=True)[0][0]