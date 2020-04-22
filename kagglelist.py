primes = [2, 3, 5, 7, 11]

planets = ['Mercury', 'venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']

hands = [
    ['J', 'Q', 'K'],
    ['2', '2', '2'],
    ['6', 'A', 'K'],  # (Comma after the last element is optional)
]

my_favorite_things = [32, 'raindrops on roses', help]

"""Indexing"""
print(planets[0])

"""Slicing"""
print(planets[0:3])
print(planets[2:])
print(planets[::-1])
print(planets[::-2])

print(max(primes))
print(min(primes))

x = 12  # x is a real number, so its imaginary part is 0
print(x.imag)
c = 12 + 3j  # here's how to make a complex number, in case you have ever been curious:
print(c.imag)

""" List Methods """
# list.append

print(planets.append('Pluto'))
print(planets)

# list.pop

print(planets.pop())
print(planets)

print("Earth" in planets)
print("Pluto" in planets)

""" Tuples """
t = (1, 2, 3)
t[0] = 100  # 'tuple' object does not support item assignment
print(t)

x = 0.125
print(x.as_integer_ratio())

y1 = 0.25
print(y1.as_integer_ratio())
