import timeout_decorator
import unittest
from exercise.person_collection import Person, PersonCollection

class PersonCollectionTests(unittest.TestCase):

    def setUp(self):
        self.people = PersonCollection()

    def add_people(self, count):
        for i in range(count):
            self.people.add_person(
                Person(name="Pesho{0}".format(str(i % 100)),
                       email="pesho{0}@gmail{1}.com".format(str(i), str(i % 100)),
                       age=i % 100,
                       town="yambol{0}".format(str(i % 100)))
            )

    @timeout_decorator.timeout(250)
    def test_performance_add_person(self):
        self.add_people(5000)
        self.assertEqual(5000, len(self.people))

    @timeout_decorator.timeout(200)
    def test_performance_find_person(self):
        self.add_people(5000)

        for _ in range(100000):
            existing_person = self.people.find_person("pesho1@gmail1.com")
            self.assertIsNotNone(existing_person)
            non_existing_person = self.people.find_person("non-existing email")
            self.assertIsNone(non_existing_person)

    @timeout_decorator.timeout(300)
    def test_performance_find_people_by_email(self):
        self.add_people(5000)

        for _ in range(10000):
            existing_people = list(self.people.find_people_by_email_domain("gmail1.com"))
            self.assertEqual(len(existing_people), 50)

            non_existing_people = self.people.find_people_by_email_domain("non-existing email")
            self.assertIsNone(non_existing_people)

    @timeout_decorator.timeout(300)
    def test_performance_find_people_by_name_and_town(self):
        self.add_people(5000)

        for _ in range(10000):
            existing_people = list(self.people.find_people_by_name_and_town("Pesho1", "yambol1"))
            self.assertEqual(len(existing_people), 50)
            non_existing_people = self.people.find_people_by_name_and_town("Non", "Existing")
            self.assertIsNone(non_existing_people)

    @timeout_decorator.timeout(300)
    def test_performance_find_people_by_age_group(self):
        self.add_people(5000)

        for _ in range(2000):
            existing_people = list(self.people.find_people_in_age_group(20, 21))
            self.assertEqual(len(existing_people), 100)
            non_existing_people = list(self.people.find_people_in_age_group(500, 600))
            self.assertEqual(len(non_existing_people), 0)

    @timeout_decorator.timeout(300)
    def test_performance_find_people_by_town_and_age_group(self):
        self.add_people(5000)

        for _ in range(5000):
            existing_people = list(self.people.find_people_in_age_group_from_town(18, 22, "yambol20"))
            self.assertEqual(len(existing_people), 50)
            non_existing_town_people = list(self.people.find_people_in_age_group_from_town(20, 30, "Missing Town"))
            self.assertEqual(len(non_existing_town_people), 0)
            non_existing_age_people = list(self.people.find_people_in_age_group_from_town(200, 300, "yambol20"))
            self.assertEqual(len(non_existing_age_people), 0)


if __name__ == '__main__':
    unittest.main()
