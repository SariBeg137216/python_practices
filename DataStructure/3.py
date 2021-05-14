"""Given a list slice it into 3 equal chunks and reverse each """

sampleList = [11, 45, 8, 23, 14, 12, 78, 45, 89]
chunks = len(sampleList) // 3
new_list = []
for i in range(0, len(sampleList), 3):
    new_list.append(sampleList[i:chunks])
    chunks *= 2
for items in new_list:
    print(items[::-1])
