"""linear_search.
"""
def linear_search(list, target):
    for i in range(0, len(list)):
        if list[i] == target:
            return i
    return None


myList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(linear_search(myList, 8))
