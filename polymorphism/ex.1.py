class animal():
    def speak(self):
        pass
class dog(animal):
    def speak(self):
        return "woof!"
class cat(animal):
    def speak(self):
        return "meow!"
def anima_speak(animal):
    return animal.speak()
dog = dog()
cat = cat()

print("dog says:-",anima_speak(dog))
print("cat says:-", anima_speak(cat))


