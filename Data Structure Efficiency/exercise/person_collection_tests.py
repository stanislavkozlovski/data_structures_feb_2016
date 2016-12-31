import unittest
from exercise.person_collection import Person, PersonCollection


class PersonCollectionTests(unittest.TestCase):
    def setUp(self):
        self.people = PersonCollection()

    def test_add_person_should_work(self):
        is_added = self.people.add_person(Person(
            name="Sunshine",
            email="little_rain@hotmail.com",
            age=30,
            town="next"
        ))

        self.assertTrue(is_added)
        self.assertEqual(len(self.people), 1)

    def test_add_person_duplicate_email_should_work(self):
        is_added = self.people.add_person(Person(
            name="Sunshine",
            email="little_rain@hotmail.com",
            age=30,
            town="next"
        ))
        is_added_second = self.people.add_person(Person(
            name="NoDiff",
            email="little_rain@hotmail.com",
            age=31,
            town="neext"
        ))

        self.assertTrue(is_added)
        self.assertFalse(is_added_second)
        self.assertEqual(len(self.people), 1)

    def test_find_existing_person_should_return_him(self):
        self.people.add_person(Person(
            name="Sunshine",
            email="little_rain@hotmail.com",
            age=30,
            town="next"
        ))
        person = self.people.find_person("little_rain@hotmail.com")

        self.assertIsNotNone(person)

    def test_find_non_existing_person_should_return_none(self):
        person = self.people.find_person("real_on_the_rise@abv.bg")
        self.assertIsNone(person)

    def test_delete_person_should_work(self):
        person_email = "ventsislavelud@abv.bg"
        self.people.add_person(
            Person(name="Hell", email=person_email, age=34, town="yambol, grada na otkachenite")
        )

        has_deleted_existing = self.people.delete_person(person_email)
        has_deleted_non_existing = self.people.delete_person(person_email)
        self.assertTrue(has_deleted_existing)
        self.assertFalse(has_deleted_non_existing)
        self.assertEqual(len(self.people), 0)

    def test_find_people_by_email_domain_should_return_matching_people(self):
        self.people.add_person(Person(
            email="pesho@gmail.com", name="Pesho", age=20, town="Plovdiv"
        ))
        self.people.add_person(Person(
            email="kiro@yahoo.co.uk", name="Kiril", age=22, town="Sofia"
        ))
        self.people.add_person(Person(
            email="mary@gmail.com", name="Maria", age=21, town="Plovdiv"
        ))
        self.people.add_person(Person(
            email="ani@gmail.com", name="Anna", age=19, town="Bourgas"
        ))

        gmail_people = self.people.find_people_by_email_domain("gmail.com")
        yahoo_people = self.people.find_people_by_email_domain("yahoo.co.uk")
        hoo_people = self.people.find_people_by_email_domain("hoo.co.uk")

        self.assertEqual(
            [person.email for person in gmail_people],
            ["ani@gmail.com", "mary@gmail.com", "pesho@gmail.com"]
        )
        self.assertEqual(
            [person.email for person in yahoo_people],
            ["kiro@yahoo.co.uk"]
        )
        self.assertEqual(hoo_people, [])

if __name__ == '__main__':
    unittest.main()