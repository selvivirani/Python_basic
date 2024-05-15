class india():
    def capital(self):
        print("new delhi is capital of india")
    def language(self):
        print("hindi is most popular ianguage in india")
    def type(self):
        print("india is devloping country")
class USA():
    def capital(self):
        print("washington,D.C is capital of USA")
    def language(self):
        print("english is primary language of USA")
    def type(self):
        print("USA devloped country")
obj_in = india()
obj_usa = USA()

for country in(obj_in , obj_usa):
    country.capital()
    country.language()
    country.type()
