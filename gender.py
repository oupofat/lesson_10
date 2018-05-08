class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__
person = Record()
person.name = input("What is your name?")
person.age = int(input("How old are you?"))
person.gender = input("What sex are you?")

print(person.name, "is ",person.age, "years old",person.gender,".")