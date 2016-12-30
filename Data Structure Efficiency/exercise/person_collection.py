from sortedcontainers import SortedDict


class Person:
    def __init__(self, email: str, name: str, age: int, town: str):
        self.email = email
        self.name = name
        self.age = age
        self.town = town

    def __eq__(self, other):
        if not isinstance(other, Person):
            raise TypeError('A Person can only be compared to another Person object!')
        return self.email == other.email

    def __hash__(self):
        return hash(self.email)


class PersonCollection:
    def __init__(self):
        self.people = {} # key: email, value: person object
        self.people_email_domain = {}
        self.people_by_name_town = {}
        self.people_by_age = SortedDict()
        # key: age, value: Dict{key:town, value:SortedDict(key:email, value:person)
        self.people_by_age_and_town = SortedDict()

    def add_person(self, person):
        if person.email in self.people:
            return False
        self.people[person.email] = person
        # add to the email domains
        self._add_to_email_domain(person)
        # add to the name_town dict
        self._add_to_name_town_dict(person)
        # add to the age dict
        self._add_to_age_dict(person)
        # add to the age_town dict
        self._add_to_age_town_dict(person)

    def _add_to_email_domain(self, person):
        """ Add the person to the dictionary of email domains and e-mails"""
        person_email_domain = person.email.split('@')[-1]
        if person_email_domain not in self.people_email_domain:
            self.people_email_domain[person_email_domain] = SortedDict()

        self.people_email_domain[person_email_domain][person.email] = person

    def _add_to_name_town_dict(self, person):
        """ Add the person to the dictionary holding people by their name+town """
        person_name_town = person.name + person.town
        if person_name_town not in self.people_by_name_town:
            self.people_by_name_town[person_name_town] = SortedDict()
        self.people_by_name_town[person_name_town][person.email] = person

    def _add_to_age_dict(self, person):
        """ Add the person to the age dictionary """
        if person.age not in self.people_by_age:
            self.people_by_age[person.age] = SortedDict()

        self.people_by_age[person.age][person.email] = person

    def _add_to_age_town_dict(self, person):
        """ add a person to the dictionary holding people by
            their age and then by their town """
        if person.age not in self.people_by_age_and_town:
            self.people_by_age_and_town[person.age] = dict()
        if person.town not in self.people_by_age_and_town[person.age]:
            self.people_by_age_and_town[person.age][person.town] = SortedDict()

        self.people_by_age_and_town[person.age][person.town][person.email] = person


jeffrey = Person(email="jeff@real_on_the-rise.com", name="Jeffrey", age=34, town="North Side of Philly")
mike = Person(email="mike@real_on_the-rise.com", name="Mikey", age=14, town="North Side of Philly")
mike_two = Person(email="arr@real_on_the-rise.com", name="Mikey", age=41, town="North Side of Philly")

rappers = PersonCollection()
rappers.add_person(jeffrey)
rappers.add_person(mike)
rappers.add_person(mike_two)
print()