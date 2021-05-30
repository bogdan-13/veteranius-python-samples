# single inheritance

class Mammal():
    className = 'Mammal'

class Dog(Mammal):
    species = 'Canis lupus'

dog = Dog()
print(dog.className) # Mammal

# multiple inheritance

class Horse():
    isHorse = True

class Donkey():
    isDonkey = True

class Mule(Horse, Donkey):
    pass

mule = Mule()
print(f'Mule is horse: {mule.isHorse}') # True
print(f'Mule is donkey: {mule.isDonkey}') # True

# For multiple inheritance to work Python builds MRO (Method Resolution Order)
# If MRO can not be built reliably program fails with exception
# Two priority rules:
# - left before right 
# - children before parents

class Bird:
    def fly():
        return 'I can fly...'

class Duck(Bird):
    def quack():
        return 'Quack!'

class RubberDuck(Bird, Duck): # TypeError: Cannot create a consistent method resolution
    pass                      # order (MRO) for bases Bird, Duck
    
