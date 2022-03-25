
nested_list = [
	['a', 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

class MyIterator:
    def __init__(self, iter_list: list):
        self.new_list = [element for item in iter_list for element in item]

    def __iter__(self):
        self.cursor = -1
        return self

    def __next__(self):
        self.cursor += 1
        if self.cursor >= len(self.new_list):
            raise StopIteration
        return self.new_list[self.cursor]


flat_list = [item for item in MyIterator(nested_list)]
print(flat_list)

for item in MyIterator(nested_list):
    print(item)

# 2 генератор
flat_list_gen = (element for list in nested_list for element in list)

for el in flat_list_gen:
	print(el, end=' ')


