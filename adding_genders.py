class Record(object):
    def __init__(self, **kw):
        self.__dict__.update(kw)

    def __repr__(self):
        return "Record%r" % self.__dict__

collect_person=[]

while True:
    person = Record()
    
    person.name = input("What is your name?")   
    person.age = int(input("How old are you?"))
    person.gender = input("What sex are you?")
    collect_person.append(person)
    
    yn = input("Wanna add another? (y or n) ")
    if yn != "y":
        break
def get_member(collect_person):
    for record in collect_person:
        print (record.name,"is", record.age, "years old",record.gender)
get_member(collect_person)   
		
		



	