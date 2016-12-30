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

    def __str__(self):
        return '{name} aged {age} from {town} - {email}'.format(name=self.name, age=self.age,
                                                                town=self.town, email=self.email)

    def __repr__(self):
        return self.__str__()


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

    def find_person(self, email: str):
        """ Return the person object or None if he does not exist"""
        if email in self.people:
            return self.people[email]
        return None

    def find_people_by_email_domain(self, email_domain: str):
        """ Returns a sequence of matches people sorted by their email"""
        if email_domain in self.people_email_domain:
            return (person for person in self.people_email_domain[email_domain].values())

    def find_people_by_name_and_town(self, name: str, town: str):
        name_and_town = name + town
        if name_and_town in self.people_by_name_town:
            return (person for person in self.people_by_name_town[name_and_town].values())

    def find_people_in_age_group(self, start_age: int, end_age: int):
        if start_age < 0 or start_age > end_age:
            raise Exception('Invalid age group!')

        keys = self.people_by_age.irange(start_age, end_age)
        return (person for age in keys for person in self.people_by_age[age].values())

    def find_people_in_age_group_from_town(self, start_age: int, end_age: int, town: str) -> iter:
        """Returns a sequence of matched persons sorted by age, then by email (as second criteria)"""
        if start_age < 0 or start_age > end_age:
            raise Exception('Invalid age group!')

        ages = self.people_by_age_and_town.irange(start_age, end_age)
        return (person for age in ages
                if town in self.people_by_age_and_town[age]
                for person in self.people_by_age_and_town[age][town].values())  # check if there is a key for that town

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
