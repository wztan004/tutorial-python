# https://realpython.com/python3-object-oriented-programming/

# Inheritance
# __str__ representation
# Check parent class instance
# Check child class instance
# Method override
# Argument override

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old"

    def speak(self, sound):
        return f"{self.name} says {sound}"
    
    def speakLoudly(self, sound):
        return f"{self.name} says {sound}"


class Terrier(Dog):
    def speak(self, sound="Arf"):
        return f"{sound} {sound} {sound}"
    
    def speakLoudly(self, sound="!!!!!"):
        return super().speakLoudly(sound)

class Dachshund(Dog):
    pass

class Bulldog(Dog):
    pass


if __name__ == "__main__":
    terrier = Terrier('dog',4) # Inheritance
    print(terrier) # __str__ representation
    print(terrier.speak('woof')) # Inheritance
    print(isinstance(terrier, Dog)) # Check parent class instance
    print(isinstance(terrier, Terrier)) # Check child class instance
    print(terrier.speak()) # Method override
    print(terrier.speakLoudly()) # Argument override