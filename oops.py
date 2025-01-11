# Single Inheritance
class animal:
    def speak(self):
        print("animals are top g's")

class dog(animal):  # Single inheritance
    def speak(self):
        print("Woof")

class cat(animal):  # Single inheritance
    def speak(self):
        print("Meow")

# Multiple Inheritance
class father:
    def speak(self):
        print("I am a father")

class mother:
    def speak(self):
        print("I am a mother")

class child(father, mother):  # Multiple inheritance
    def child_traits(self):
        print("traits from child")

# Multilevel Inheritance
class grandchild(child):  # Multilevel inheritance
    def grandchild_traits(self):
        print("traits from grandchild")

# Hierarchical Inheritance (already shown with dog and cat)

# Hybrid Inheritance (combination of multiple and multilevel)
class hybrid_child(father, mother):  # Multiple inheritance
    def hybrid_traits(self):
        print("traits from hybrid child")

class hybrid_grandchild(hybrid_child):  # Multilevel inheritance
    def hybrid_grandchild_traits(self):
        print("traits from hybrid grandchild")

# Testing the code
d = dog()
d.speak()  # Output: Woof

c = cat()
c.speak()  # Output: Meow

ch = child()
ch.speak()  # Output: I am a father (due to MRO)

gc = grandchild()
gc.speak()  # Output: I am