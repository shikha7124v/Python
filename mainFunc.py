def func():
    print("Hi there!!")

print(__name__)
if __name__ == "__main__":
    func()

'''The if __name__ == "__main__": idom is a common pattern used in python scripts to determine 
whether the script is being rundirectly or being imported as a module into another script.'''

'''In python the __name__ variable is a built-in variable that is automatically set to the name
of the current module. When the python script is run directly, the __name__ variable is set 
to the string __main__. When the script is imported as a module into another script, the __name__ 
variable is set to the name of the module. '''