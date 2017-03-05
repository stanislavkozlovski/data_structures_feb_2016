"""
Write a program that receives some info from the console about people and their phone numbers.
You are free to choose the manner in which the data is entered;
each entry should have just one name and one number (both of them strings).

After filling this simple phonebook, upon receiving the command "search",
your program should be able to perform a search of a contact by name and print her details in format "{name} -> {number}".
In case the contact isn't found, print "Contact {name} does not exist." Examples:
"""
from exercises.chaining_hash_table import HashTable


SEARCH_KEYWORD = 'search'
phonebook = HashTable()
user_input = input()

# fills the dict
while user_input != SEARCH_KEYWORD:
    user, phone = user_input.split('-')
    phonebook.add_or_replace(user, phone)
    user_input = input()

while True:
    wanted_user_phone = input()
    phone, result = phonebook.try_get_value(wanted_user_phone)
    if result:
        print("{name} -> {phone}".format(
            name=wanted_user_phone, phone=phone
        ))
    else:
        print("Contact {user} does not exist.".format(
            user=wanted_user_phone
        ))
