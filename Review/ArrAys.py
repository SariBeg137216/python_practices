import array as arr


class ArrAy(object):

    def __init__(self, data):
        self.array = data

    def AddElement(self, index, element):
        new_array = []
        for i in range(index):
            new_array.insert(i, self.array[i])

        new_array.insert(index, element)

        x = index + 1
        while x <= len(self.array):
            new_array.insert(x, self.array[x - 1])
            x += 1
        return new_array

    def Search(self, arrr, elemet):
        for i in range(len(arrr)):
            if arrr[i] == elemet:
                return i

    def Delete(self, arrr, element):
        value = self.Search(arrr, element)
        del arrr[value]
        return arrr


x = ArrAy([1, 2, 5, 7, 3, 9])
new_array = x.AddElement(4, 15)
# print(new_array)
# print(x.Search(new_array, 3))
print(x.Delete(new_array, 2))