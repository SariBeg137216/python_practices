"""Initialize dictionary with default values"""

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}
print(dict.fromkeys(employees, defaults))
resDict = dict.fromkeys(employees, defaults)
print(resDict)


