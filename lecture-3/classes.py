class Dog: #* new type of object
    #* members/attributes of a class

    default_sound = "Woof-woof"                          #* static/class fields/properties

    def __init__(self, bark_sound):                      #* constructor
        self.bark_sound = bark_sound                     #* instance fields/properties

    def __str__(self):
        return f"Dog: {self.bark()}"

    def bark(self):
        return self.bark_sound                           #* instance methods/bound function        

    @staticmethod
    def default_bark():                                  #* static method/associative function
        return Dog.default_sound

    @classmethod                                         #* class method
    def my_shiny_class_method(cls, value):
        return cls.my_shiny_static_field

dog_charlie = Dog("Loud barking...")
dog_bravo = Dog("Not so loud barking...")

print(dog_charlie.bark()) # Loud barking...
print(dog_bravo.default_bark()) # Woof-woof
print(Dog.default_bark()) # Woof-woof
print(dog_bravo) # Dog: Not so loud barking...