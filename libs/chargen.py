# RPG Character Lab
# https://www.freecodecamp.org/learn/python-v9/lab-rpg-character/build-an-rpg-character
full_dot = '●'
empty_dot = '○'


def create_character(name, strength, intelligence, charisma):
    # check character name
    if not isinstance(name, str):
        return "The character name should be a string"

    if name == "":
        return "The character should have a name"

    if len(name) > 10:
        return "The character name is too long"

    if " " in name:
        return "The character name should not contain spaces"

    # check stats
    for stat in (strength, intelligence, charisma):
        if not isinstance(stat, int):
            return "All stats should be integers"
        if stat < 1:
            return "All stats should be no less than 1"
        if stat > 4:
            return "All stats should be no more than 4"

    # starting stats pool
    if (strength + intelligence + charisma) != 7:
        return "The character should start with 7 points"

    # output stats with visual dots
    def stat_bar(value):
        return full_dot * value + empty_dot * (10 - value)

    # Format output
    return f"{name}\nSTR {stat_bar(strength)}\nINT {stat_bar(intelligence)}\nCHA {stat_bar(charisma)}"
