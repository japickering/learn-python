from shared.planet import Planet

# create planets
planet_1 = Planet('Earth', 'Homeworld', 'Sun')
planet_2 = Planet('Mars', 'Terrestrial', 'Sun')
planet_3 = Planet('Jupiter', 'Gas Giant', 'Sun')

# Print the planets and their orbits
for p in [planet_1, planet_2, planet_3]:
    print(p)
    print(p.orbit())
