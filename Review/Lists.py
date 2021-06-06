# sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
# chunk = len(sampleList) // 3
# for i in range(0, len(sampleList), 3):
#     ch = sampleList[i:chunk:]
#     chunk += 3
#
#     print(ch[::-1])

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]

# dictionary = {k: v for k, v in zip(keys, values)}
# dictionary = dict(zip(keys, values))
# print(dictionary)

# employees = ['Kelly', 'Emma', 'John']
# defaults = {"designation": 'Application Developer', "salary": 8000}
#
# resD = dict.fromkeys(employees, defaults)
# print(resD)

# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
#
# }

# keysToRemove = ["name", "salary"]
#
# print({i: sampleDict[i] for i in sampleDict.keys() - keysToRemove})
#
# sampleDict = {
#     "name": "Kelly",
#     "age": 25,
#     "salary": 8000,
#     "city": "New york"
# }
#
# del sampleDict['city']  # my solution
# sampleDict.update({'location': 'New york'})
# print(sampleDict)
# sampleDict['location'] = sampleDict.pop('city')  # exercise solution

sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(sampleDict.items())
values = []
for k, v in sampleDict.items():
    values.append(k)

print(min(values, key=sampleDict.get))

sampleDict.update({'history': 80})
print(sampleDict)

