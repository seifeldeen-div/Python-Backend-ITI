def count_vowels(arr):
    counter = 0
    vowels = ['a', 'e', 'i', 'o','u']
    for i in arr:
        for v in vowels:
            if i == v:
                counter += 1
    return counter
print((count_vowels('Hello World')))

# -----------------------------------------------------------------------------------------

def find_char_locations(string):
    indexList = []
    trans = list(string)
    for i in range (len(trans)):
        if trans[i] == 'i' or trans[i] == 'I':
            indexList.append(i)
    return indexList
print(find_char_locations('iti summer training'))

# -----------------------------------------------------------------------------------------

def first_and_last(string):
    str1 = string[0]
    str2 = string[len(string) - 1]
    return str1 + str2
print(first_and_last('Python'))

# -----------------------------------------------------------------------------------------

list_number = []
for i in range(5):
    list_number.append(int(input()))
list_number.sort()
print(list_number)
list_number.sort(reverse=True)
print(list_number)

# -----------------------------------------------------------------------------------------

def remove_duplicates(list_numbers):
    set_numbers = set(list_numbers)
    counter  = len(list_numbers) - len(set_numbers)
    return list(set_numbers) , counter
print(remove_duplicates([1, 2, 3, 2, 4, 1, 5]))

# -----------------------------------------------------------------------------------------

def unpack_and_sum(numbers):
    f, *m, l = numbers
    return f, sum(m), l

result = list(unpack_and_sum((10, 20, 30, 40, 50)))
f, m, l = result
print("First:", f)
print("Last:", l)
print("middle:", m)

# -----------------------------------------------------------------------------------------

def lists_to_dict(keys,values):
    combine = {}
    for i in range(len(keys)):
        combine[keys[i]] = values[i]
    return combine
print(lists_to_dict(['name', 'age', 'city'], ['Ali', 25, 'Cairo']))

# -----------------------------------------------------------------------------------------

def filter_and_inflate(items):
    result = {}
    for item in items:
        if items[item] > 50:
            result[item] = items[item] * 1.10
    return result

print(filter_and_inflate({'apple': 30, 'banana': 60, 'orange': 80}))

# -----------------------------------------------------------------------------------------

def find_palindromes(words):
    result = set(words)

    for word in words:
        if word == word[::-1]:
            result.add(word)
    return result

print(find_palindromes(['level', 'hello', 'radar', 'world', 'civic']))

# -----------------------------------------------------------------------------------------

# f_set = frozenset( [ (1, 2) , (3, 4), (5, 6) ] )
def check_coordinate(f_set, check):
    for coordinate in f_set:
        if coordinate == check:
            return True
    return False
f_set = frozenset([(1, 2), (3, 4), (5, 6)])

print(check_coordinate(f_set, (3, 4)))
print(check_coordinate(f_set, (7, 8)))

# -----------------------------------------------------------------------------------------
