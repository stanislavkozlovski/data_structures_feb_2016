"""
Solve the next problems by using the implemented dictionary.
 You are NOT allowed to use the built-in Dictionary or SortedDictionary classes!

Write a program that reads some text from the console and counts the occurrences of each character in it.
Print the results in alphabetical (lexicographical) order. Examples:
"""

from exercises.chaining_hash_table import HashTable

text = input()
dictionary = HashTable(len(text) * 2)  # make sure it doesn't need to grow

for c in text:
    if not dictionary.has_key(c):
        dictionary[c] = 0
    dictionary[c] += 1

for letter, occ in sorted(dictionary, key=lambda x: x.key):
    print('{letter}: {occ_count} time/s'.format(
        letter=letter,
        occ_count=occ
    ))