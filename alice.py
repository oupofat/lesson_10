class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__
person = Record(name="Alice", age=7)
print(person.name, "is", person.age, "years old.")