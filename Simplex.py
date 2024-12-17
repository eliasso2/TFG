import math

'''
class Complexe():
    def __init__(self, dim):
        self.dim = dim

    def enganxa(self, c)
'''
    
class Simplex():
    def __init__(self, dim, cares = []):
        self.dim = dim
        self.cares = cares
        for i in range(dim + 1 - len(cares)):
            self.cares.append(Simplex(dim - 1))

    def enganxa_simplex(self, s):
        for i in range(len(self.cares)):
            s.cares.insert(i, self.cares[i])
            s.cares.pop(i + 1)
            