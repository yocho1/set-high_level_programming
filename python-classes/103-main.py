#!/usr/bin/python3
MagicClass = __import__('103-magic_class').MagicClass

circle = MagicClass(5)
print("Area:", circle.area())
print("Circumference:", circle.circumference())

try:
    invalid = MagicClass("hello")
except Exception as e:
    print(e)
