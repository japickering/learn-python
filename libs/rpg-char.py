# RPG Character Lab
# https://www.freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character
# Objective: Fulfill the user stories below and get all the tests to pass to complete the lab.

# User Stories:

# You should have a function named create_character.
# The function should accept, in order, a character name followed by three stats: strength, intelligence, and charisma.
# The character name should be validated:
# If the character name is not a string, the function should return The character name should be a string.
# If the character name is an empty string, the function should return The character should have a name.
# If the character name is longer than 10 characters, the function should return The character name is too long.
# If the character name contains spaces, the function should return The character name should not contain spaces.

# The stats should also be validated:
# If one or more stats are not integers, the function should return All stats should be integers.
# If one or more stats are less than 1, the function should return All stats should be no less than 1.
# If one or more stats are more than 4, the function should return All stats should be no more than 4.
# If the sum of all stats is different than 7, the function should return The character should start with 7 points.
# If all values pass the verification, the function should return a string with four lines:
# the first line should contain the character name
# lines 2-4 should start with the stat abbreviation, STR, INT or CHA (in this order), then a space, and then a number of full dots (●) equal to the value of the stat, and a number of empty dots (○) to reach 10. Example: if the value of strength is 3 there must be 3 full dots followed by 7 empty dots. The dots are given in the editor.

# Here's the string that should be returned by create_character('ren', 4, 2, 1):

full_dot = '●'
empty_dot = '○'


def dots(max: int):
    v = ''
    for x in range(max):
        v += full_dot

    return v


def dots_empty(max: int):
    v = ''
    for x in range(max):
        v += empty_dot

    return v


def format(name: str, strength: int, intelligence: int, charisma: int):
    output = f'{name}\nSTR {dots(strength)}{dots_empty(6)}\nINT {dots(intelligence)}{dots_empty(8)}\nCHA {dots(charisma)}{dots_empty(9)}'
    return output


def create_character(name: str, strength: int, intelligence: int, charisma: int):
    if name == '':
        return 'The character should have a name'

    if type(name) is not str:
        return 'The character name should be a string'

    if type(name) is str and len(name) > 10:
        return 'The character name is too long'

    if ' ' in name:
        return 'The character name should not contain spaces'

    if not all(isinstance(x, int) for x in [strength, intelligence, charisma]):
        return 'All stats should be integers'

    if any(x < 1 for x in [strength, intelligence, charisma]):
        return 'All stats should be no less than 1'

    if any(x > 4 for x in [strength, intelligence, charisma]):
        return 'All stats should be no more than 4'

    if sum([strength, intelligence, charisma]) != 7:
        return 'The character should start with 7 points'

    print(format(name, strength, intelligence, charisma))


create_character('ren', 4, 2, 1)
