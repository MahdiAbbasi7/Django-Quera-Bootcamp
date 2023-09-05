"""
repeat in itertools

repeat an object for mant times(you can add your time).
repeat is a lazy object.
for many iterations this is usefull because is optimal.
"""

from itertools import repeat

name = "Mahdi"

print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))
print(next(repeat(name)))

