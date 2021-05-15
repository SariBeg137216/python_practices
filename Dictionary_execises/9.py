"""Get the key of a minimum value from the following dictionary"""


sampleDict = {
    'Physics': 82,
    'Math': 65,
    'history': 75
}
print(min(sampleDict, key=sampleDict.get))
# val = min(sampleDict.values())
# for k in sampleDict.keys():
#     if sampleDict[k] == val:
#         print(k)