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

    def test_find_people_by_name_and_town_should_return_matching_people(self):
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
        self.people.add_person(Person(
            email="pepi2@yahoo.fr", name="Pesho", age=21, town="Plovdiv"
        ))

        people_pesho_plovdiv = self.people.find_people_by_name_and_town("Pesho", "Plovdiv")
        people_lower_case = self.people.find_people_by_name_and_town("pesho", "plovdiv")
        people_pesho_no_town = self.people.find_people_by_name_and_town("Pesho", None)
        people_anna_bourgas = self.people.find_people_by_name_and_town("Anna", "Bourgas")

        self.assertEqual(
            [person.email for person in people_pesho_plovdiv],
            ["pepi2@yahoo.fr", "pesho@gmail.com"]
        )
        self.assertEqual(
            people_lower_case,
            []
        )
        self.assertEqual(
            people_pesho_no_town,
            []
        )
        self.assertEqual(
            [person.email for person in people_anna_bourgas],
            ["ani@gmail.com"]
        )

    def test_find_people_by_age_group_should_return_matching_people(self):
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
        self.people.add_person(Person(
            email="pepi2@yahoo.fr", name="Pesho", age=21, town="Plovdiv"
        ))
        self.people.add_person(Person(
            email="asen@gmail.com", name="Asen", age=21, town="Rousse"
        ))

        people_aged_21_to_22 = self.people.find_people_in_age_group(21, 22)
        people_aged_10_11 = self.people.find_people_in_age_group(10, 11)
        people_aged_21 = self.people.find_people_in_age_group(21, 21)
        people_aged_19 = self.people.find_people_in_age_group(19, 19)
        people_aged_0_to_1000 = self.people.find_people_in_age_group(0, 1000)

        self.assertEqual(
            [person.email for person in people_aged_21_to_22],
            ["asen@gmail.com", "mary@gmail.com", "pepi2@yahoo.fr", "kiro@yahoo.co.uk"]
        )

        self.assertEqual(
            [person.email for person in people_aged_10_11],
            []
        )

        self.assertEqual(
            [person.email for person in people_aged_21],
            ["asen@gmail.com", "mary@gmail.com", "pepi2@yahoo.fr"]
        )

        self.assertEqual(
            [person.email for person in people_aged_19],
            ["ani@gmail.com"]
        )

        self.assertEqual(
            [person.email for person in people_aged_0_to_1000],
            ["ani@gmail.com", "pesho@gmail.com", "asen@gmail.com", "mary@gmail.com", "pepi2@yahoo.fr",
             "kiro@yahoo.co.uk"]
        )

    def test_find_people_by_age_group_and_town_should_return_matching_people(self):
        self.people.add_person(Person("pesho@gmail.com", "Pesho", 28, "Plovdiv"))
        self.people.add_person(Person("kirosofia@yahoo.co.uk", "Kiril", 22, "Sofia"))
        self.people.add_person(Person("kiro@yahoo.co.uk", "Kiril", 22, "Plovdiv"))
        self.people.add_person(Person("pepi@gmail.com", "Pesho", 21, "Plovdiv"))
        self.people.add_person(Person("ani@gmail.com", "Anna", 19, "Bourgas"))
        self.people.add_person(Person("ani17@gmail.com", "Anna", 17, "Bourgas"))
        self.people.add_person(Person("pepi2@yahoo.fr", "Pesho", 21, "Plovdiv"))
        self.people.add_person(Person("asen.rousse@gmail.com", "Asen", 21, "Rousse"))
        self.people.add_person(Person("asen@gmail.com", "Asen", 21, "Plovdiv"))

        people_aged_from_21_22_plovdiv = self.people.find_people_in_age_group_from_town(21, 22, "Plovdiv")
        self.assertEqual(
            [person.email for person in people_aged_from_21_22_plovdiv],
            ["asen@gmail.com", "pepi2@yahoo.fr", "pepi@gmail.com", "kiro@yahoo.co.uk"]
        )

        people_aged_from_10_11_sofia = self.people.find_people_in_age_group_from_town(10, 11, "Sofia")
        self.assertEqual(
            [person.email for person in people_aged_from_10_11_sofia],
            []
        )

        people_aged_21_plovdiv = self.people.find_people_in_age_group_from_town(21, 21, "Plovdiv")
        self.assertEqual(
            [person.email for person in people_aged_21_plovdiv],
            ["asen@gmail.com", "pepi2@yahoo.fr", "pepi@gmail.com"]
        )

        people_aged_19_bourgas = self.people.find_people_in_age_group_from_town(19, 19, "Bourgas")
        self.assertEqual(
            [person.email for person in people_aged_19_bourgas],
            ["ani@gmail.com"]
        )

        people_aged_from_0_1000_plovdiv = self.people.find_people_in_age_group_from_town(0, 1000, "Plovdiv")
        self.assertEqual(
            [person.email for person in people_aged_from_0_1000_plovdiv],
            ["asen@gmail.com", "pepi2@yahoo.fr", "pepi@gmail.com", "kiro@yahoo.co.uk", "pesho@gmail.com"]
        )

        people_aged_from_0_1000_newyork = self.people.find_people_in_age_group_from_town(0, 1000, "New York")
        self.assertEqual(
            [person.email for person in people_aged_from_0_1000_newyork],
            []
        )

    def test_find_deleted_people_should_return_empty_collection(self):
        self.people.add_person(Person("pesho@gmail.com", "Pesho", 28, "Plovdiv"))
        self.people.add_person(Person("kirosofia@yahoo.co.uk", "Kiril", 22, "Sofia"))
        self.people.add_person(Person("kiro@yahoo.co.uk", "Kiril", 22, "Plovdiv"))
        self.people.add_person(Person("pepi@gmail.com", "Pesho", 21, "Plovdiv"))
        self.people.add_person(Person("ani@gmail.com", "Anna", 19, "Bourgas"))
        self.people.add_person(Person("ani17@gmail.com", "Anna", 17, "Bourgas"))
        self.people.add_person(Person("pepi2@yahoo.fr", "Pesho", 21, "Plovdiv"))
        self.people.add_person(Person("asen.rousse@gmail.com", "Asen", 21, "Rousse"))
        self.people.add_person(Person("asen@gmail.com", "Asen", 21, "Plovdiv"))

        self.people.delete_person("pesho@gmail.com")
        self.people.delete_person("kirosofia@yahoo.co.uk")
        self.people.delete_person("kiro@yahoo.co.uk")
        self.people.delete_person("pepi@gmail.com")
        self.people.delete_person("ani@gmail.com")
        self.people.delete_person("ani17@gmail.com")
        self.people.delete_person("pepi2@yahoo.fr")
        self.people.delete_person("asen.rousse@gmail.com")
        self.people.delete_person("asen@gmail.com")

        people_pesho_gmail = self.people.find_person("pesho@gmail.com")
        self.assertIsNone(people_pesho_gmail)

        people_gmail = list(self.people.find_people_by_email_domain("gmail.com"))
        people_yahoo = list(self.people.find_people_by_email_domain("yahoo.co.uk"))
        self.assertEqual(len(people_gmail), 0)
        self.assertEqual(len(people_yahoo), 0)

        people_pesho_plovdiv = list(self.people.find_people_by_name_and_town("Pesho", "Plovdiv"))
        self.assertEqual(len(people_pesho_plovdiv), 0)

        people_aged_21_22 = list(self.people.find_people_in_age_group(21, 22))
        people_aged_0_1000 = list(self.people.find_people_in_age_group(0, 1000))
        self.assertEqual(len(people_aged_21_22), 0)
        self.assertEqual(len(people_aged_0_1000), 0)

        people_aged_21_22_plovdiv = list(self.people.find_people_in_age_group_from_town(21, 22, "Plovdiv"))
        people_aged_19_bourgas = list(self.people.find_people_in_age_group_from_town(19, 19, "Bourgas"))
        self.assertEqual(len(people_aged_21_22_plovdiv), 0)
        self.assertEqual(len(people_aged_19_bourgas), 0)

    def test_multiple_operations_should_work(self):
        is_added = self.people.add_person(Person(
            email="pesho@gmail.com", name="Pesho", age=28, town="Plovdiv"
        ))
        self.assertTrue(is_added)
        self.assertEqual(len(self.people), 1)

        is_added = self.people.add_person(Person(
            email="pesho@gmail.com", name="Pesho2", age=222, town="Plovdiv222"
        ))
        self.assertFalse(is_added)
        self.assertEqual(len(self.people), 1)

        self.people.add_person(Person(
            email="kiro@yahoo.co.uk", name="Kiril", age=22, town="Plovdiv"
        ))
        self.assertEqual(len(self.people), 2)

        self.people.add_person(Person(
            email="asen@gmail.com", name="Asen", age=22, town="Sofia"
        ))
        self.assertEqual(len(self.people), 3)

        person = self.people.find_person("non-existing guy")
        self.assertIsNone(person)

        person = self.people.find_person("pesho@gmail.com")
        self.assertIsNotNone(person)
        self.assertEqual(person.email, "pesho@gmail.com")
        self.assertEqual(person.name, "Pesho")
        self.assertEqual(person.age, 28)
        self.assertEqual(person.town, "Plovdiv")

        gmail_people = self.people.find_people_by_email_domain("gmail.com")
        self.assertEqual(
            [person.email for person in gmail_people],
            ["asen@gmail.com", "pesho@gmail.com"]
        )

        people_pesho_plovdiv = self.people.find_people_by_name_and_town("Pesho", "Plovdiv")
        self.assertEqual(
            [person.email for person in people_pesho_plovdiv],
            ["pesho@gmail.com"]
        )

        people_pesho_sofia = list(self.people.find_people_by_name_and_town("Pesho", "Sofia"))
        self.assertEqual(len(people_pesho_sofia), 0)

        people_kiro_plovdiv = list(self.people.find_people_by_name_and_town("Kiro", "Plovdiv"))
        self.assertEqual(len(people_kiro_plovdiv), 0)

        people_aged_22_28 = self.people.find_people_in_age_group(22, 28)
        self.assertEqual(
            [person.email for person in people_aged_22_28],
            ["asen@gmail.com", "kiro@yahoo.co.uk", "pesho@gmail.com"]
        )

        people_aged_22_28_plovdiv = self.people.find_people_in_age_group_from_town(22, 28, "Plovdiv")
        self.assertEqual(
            [person.email for person in people_aged_22_28_plovdiv],
            ["kiro@yahoo.co.uk", "pesho@gmail.com"]
        )

        is_deleted = self.people.delete_person("pesho@gmail.com")
        self.assertTrue(is_deleted)

        is_deleted = self.people.delete_person("pesho@gmail.com")
        self.assertFalse(is_deleted)

        person = self.people.find_person("pesho@gmail.com")
        self.assertIsNone(person)

        gmail_people = self.people.find_people_by_email_domain("gmail.com")
        self.assertEqual(
            [person.email for person in gmail_people],
            ["asen@gmail.com"]
        )

        people_pesho_plovdiv = self.people.find_people_by_name_and_town("Pesho", "Plovdiv")
        self.assertEqual(
            [person.email for person in people_pesho_plovdiv],
            []
        )

        people_pesho_sofia = self.people.find_people_by_name_and_town("Pesho", "Sofia")
        self.assertEqual(
            [person.email for person in people_pesho_sofia],
            []
        )

        people_kiro_plovdiv = self.people.find_people_by_name_and_town("Kiro", "Plovdiv")
        self.assertEqual(
            [person.email for person in people_kiro_plovdiv],
            []
        )

        people_aged_22_28 = self.people.find_people_in_age_group(22, 28)
        self.assertEqual(
            [person.email for person in people_aged_22_28],
            ["asen@gmail.com", "kiro@yahoo.co.uk"]
        )

        people_aged_22_28_plovdiv = self.people.find_people_in_age_group_from_town(22, 28, "Plovdiv")
        self.assertEqual(
            [person.email for person in people_aged_22_28_plovdiv],
            ["kiro@yahoo.co.uk"]
        )


if __name__ == '__main__':
    unittest.main()
