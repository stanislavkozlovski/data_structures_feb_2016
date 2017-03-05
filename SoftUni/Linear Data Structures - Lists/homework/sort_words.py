"""
Write a program that reads from the console a sequence of words (strings on a single line, separated by a space).
Sort them alphabetically. Keep the sequence in List<string>.
"""
print(' '.join(sorted(input().split())))

"""
Input
Output

wow softuni alpha
alpha softuni wow

hi
hi

rakiya beer wine vodka whiskey
beer rakiya vodka whiskey wine
"""