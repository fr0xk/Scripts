# Human Class Example

This example demonstrates how object-oriented programming (OOP) can be used to create a Human class with methods for common actions such as speaking, walking, eating, sleeping, and working.

## Basic Script

```python

def create_human(name, age, gender, height):

    return {

        "name": name,

        "age": age,

        "gender": gender,

        "height": height

    }

def speak(human, message):

    print(human["name"] + " says: " + message)

def walk(human):

    print(human["name"] + " is walking")

def eat(human, food):

    print(human["name"] + " is eating " + food)

def sleep(human):

    print(human["name"] + " is sleeping")

# create a human object and perform actions

john = create_human("John", 25, "Male", 180)

speak(john, "Hello, world!")

walk(john)

eat(john, "pizza")

sleep(john)

# add a new action for humans - working

def work(human):

    print(human["name"] + " is working")

work(john)

```

The above code shows a basic implementation of the Human class using simple Python functions. While this code may work for a small number of objects, it quickly becomes unwieldy when working with large numbers of humans or when more complex behaviors need to be added.

## OOP Script

```python

class Human:

    def __init__(self, name, age, gender, height):

        self.name = name

        self.age = age

        self.gender = gender

        self.height = height

    def speak(self, message):

        print(self.name + " says: " + message)

    def walk(self):

        print(self.name + " is walking")

    def eat(self, food):

        print(self.name + " is eating " + food)

    def sleep(self):

        print(self.name + " is sleeping")

    def work(self):

        print(self.name + " is working")

# create a human object and perform actions

john = Human("John", 25, "Male", 180)

john.speak("Hello, world!")

john.walk()

john.eat("pizza")

john.sleep()

# add a new action for humans - working

john.work()

```

In contrast, the above code shows an OOP-based implementation of the Human class, which allows for more elegant and scalable code. In this implementation, the Human class is defined with methods for common actions such as speaking, walking, eating, sleeping, and working. 

By using OOP concepts such as encapsulation, abstraction, inheritance, and polymorphism, we can easily represent real-world entities and add new behaviors and actions to our objects without modifying existing code.

For example, adding a new action to the Human class in the OOP script is as simple as defining a new method and calling it on each object, while in the basic script, we would need to modify the function definition and call it for each object.

```python


# add a new action for humans - dancing

class Human:

    def __init__(self, name, age, gender, height):

        self.name = name

        self.age = age

        self.gender = gender

        self.height = height

    def speak(self, message):

        print(self.name + " says: " + message)

    def walk(self):

        print(self.name + " is walking")

    def eat(self, food):

        print(self.name + " is eating " + food)

    def sleep(self):

        print(self.name + " is sleeping")

    def work(self):

        print(self.name + " is working")

    def dance(self):

        print(self.name + " is dancing")

# create a human object and perform actions

john = Human("John", 25, "Male", 180)

john.speak("Hello, world!")

john.walk()

john.eat("pizza")

john.sleep()

john.work()

john.dance()














--------
# add a new action for humans - dancing

class Human:

    def __init__(self, name, age, gender, height):

        self.name = name

        self.age = age

        self.gender = gender

        self.height = height

    def speak(self, message):

        print(self.name + " says: " + message)

    def walk(self):

        print(self.name + " is walking")

    def eat(self, food):

        print(self.name + " is eating " + food)

    def sleep(self):

        print(self.name + " is sleeping")

    def work(self):

        print(self.name + " is working")

    def dance(self):

        print(self.name + " is dancing")

# create a human object and perform actions

john = Human("John", 25, "Male", 180)

john.speak("Hello, world!")

john.walk()

john.eat("pizza")

john.sleep()

john.work()

john.dance()

# add a new action for humans - dancing

class Human:

    def __init__(self, name, age, gender, height):

        self.name = name

        self.age = age

        self.gender = gender

        self.height = height

    def speak(self, message):

        print(self.name + " says: " + message)

    def walk(self):

        print(self.name + " is walking")

    def eat(self, food):

        print(self.name + " is eating " + food)

    def sleep(self):

        print(self.name + " is sleeping")

    def work(self):

        print(self.name + " is working")

    def dance(self):

        print(self.name + " is dancing")

# create a human object and perform actions

john = Human("John", 25, "Male", 180)

john.speak("Hello, world!")

john.walk()

john.eat("pizza")

john.sleep()

john.work()

john.dance()

```

