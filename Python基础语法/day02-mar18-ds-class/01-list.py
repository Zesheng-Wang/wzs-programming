numbers = [1, 2, 3, 4, 5]
numbers[0]  # returns the first item
numbers[1]  # returns the second item
numbers[-1]  # returns the first item from the end
numbers[-2]  # returns the second item from the end
numbers.append(6)  # adds 6 to the end
numbers.insert(0, 6)  # adds 6 at index position of 0
numbers.remove(6)  # removes 6
numbers.pop()  # removes the last item
numbers.clear()  # removes all the items
numbers.sort()  # sorts the list
numbers.reverse()  # reverses the list
numbers.copy()  # returns a copy of the list


numbers = [1, 2, 3, 4, 5]
first, second, *other = numbers

letters = ["a", "b", "c"]
for letter in letters:
    print(letter)
letters = ["a", "b", "c"]
for letter in enumerate(letters):
    print(letter)
numbers = [3, 51, 2, 8, 6]
numbers.sort(reverse=True)
print(sorted(numbers, reverse=True))

# 复杂排序
items = [("Product1", 10), ("Product2", 9), ("Product3", 2)]


def sort_item(item):
    return item[1]


# items.sort(key = sort_item)
items.sort(key=lambda item: item[1])
print(items)
items = [("Product1", 10), ("Product2", 9), ("Product3", 2)]

prices = []
for item in items:
    prices.append(item[1])
print(prices)

x = list(map(lambda item: item[1], items))
print(x)
items = [("Product1", 10), ("Product2", 9), ("Product3", 12)]


x = list(filter(lambda item: item[1] >= 10, items))
print(x)
