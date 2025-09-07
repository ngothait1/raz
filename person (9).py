class Person:
    def __init__ (self):
        self.id = ""
        self.name = ""
        self.age = ""
        Person.persons = {} 
        Person.data = {} 
        Person.persons_id_list = [] 
        Person.total_age = 0 
        Person.person_count = 0 
        Person.search = None
        Person.person = {}
        Person.idByIndex = None 
