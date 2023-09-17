# Write a python progrm to import a built-in arry module and display the namespace of the said module.
import array
for name in array.__dict__:
    print(name)