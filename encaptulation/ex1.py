class encap:
    def __init__(self):
        self._k = 7
class enc(encap):
    def __init__(self):
        encap.__init__(self)
        print("calling protecyed member:-",self._k)

        self._k = 77
        print("calling protected member:-",self._k)
obj = encap()
obj2 = enc()

print("accessing protected member:-",obj._k)
print("accessing protected member:-",obj2._k)
