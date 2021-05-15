"""
 Create a new dictionary by extracting the following keys from a below dictionary
"""
sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keys = ["name", "salary"]
print({k: sampleDict[k] for k in keys})


