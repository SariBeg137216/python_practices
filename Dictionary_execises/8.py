""" Rename key city to location in the following dictionary"""

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"
}


sampleDict.setdefault('location', 'New york')

city = {k: sampleDict[k] for k in sampleDict.keys() if k == 'city'}
print(dict(sampleDict.items() - city.items()))


sampleDict['location'] = sampleDict.pop('city')
print(sampleDict)