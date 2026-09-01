# Build a Planet class in Python
class Planet():
    def __init__(self, name: str, planet_type: str, star: str):
        self.name = name
        self.planet_type = planet_type
        self.star = star

        if not isinstance(name, str) or not isinstance(planet_type, str) or not isinstance(star, str):
            raise TypeError('name, planet type, and star must be strings')

        if name == '' or planet_type == '' or star == '':
            raise ValueError(
                'name, planet_type, and star must be non-empty strings')

    def orbit(self):
        return f'{self.name} is orbiting around {self.star}...'

    def __str__(self):
        name = self.name
        planet_type = self.planet_type
        star = self.star
        return f'Planet: {name} | Type: {planet_type} | Star: {star}'
