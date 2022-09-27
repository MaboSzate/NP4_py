import numpy as np


class RandomBag:

    def __init__(self, seed=0):
        self.content = []
        np.random.seed(seed)

    def __str__(self):
        return "[RandomBag] : " + str(self.content)

    def __add__(self, other):
        return self.content + other.content

    def put(self, object):
        self.content.append(object)

    def pop(self):

        if len(self.content) > 0:
            index = np.random.randint(0, len(self.content))
            item = self.content[index]
            del self.content[index]
            return item
        else:
            return "Üres a táska"

    def size(self):
        return len(self.content)


bag = RandomBag()

for iiii in range(1, 11):
    bag.put(iiii)

print(bag + bag)

while bag.size() > 0:
    print(bag.pop())
