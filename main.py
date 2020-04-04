def first_to_last(collection):
    collection.append(collection.pop(0))
    return collection


print(first_to_last([1, 2, 3, 4]))
print(first_to_last(["python", "is", "awesome"]))
print(first_to_last(["strawberry", "kiwi", "mango", "guava"]))
