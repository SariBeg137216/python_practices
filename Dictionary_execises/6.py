"""Delete set of keys from a dictionary"""
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

new_dict = {k: sampleDict[k] for k in sampleDict.keys() - keysToRemove}
print(new_dict)
