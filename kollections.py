# 1. Counter - This stores elements as dictionary keys and counts as dictionary values.
# CounterS create a hash table in which the elements and their count are stored as dictionary keys and value pairs.

from collections import Counter
something = 'aaaaabbbbccc'
myCounter = Counter(something)
print(f"\n{myCounter}")

# items, keys and values
print(f"\n{myCounter.items()}")
print(f"\n{myCounter.keys()}")
print(f"\n{myCounter.values()}\n")

# most common types
print(f"\n{myCounter.most_common(2)}")

# most common items
print(f"\n{myCounter.most_common(2)[0]}")

# most common element
print(f"\n{myCounter.most_common(2)[0][0]}")

# all elements as a list
print(f"\n{list(myCounter.elements())}")

# 2. nametuple - Creates a tuple with named fields similar to regular tuples.

from collections import namedtuple

# create a class called Point with fields x and y
Point = namedtuple('Point', 'x,y')
pt = Point(2, 10)
print(f"\n{pt}")

# access the fields
print(f"\n{pt.x, pt.y}\n")
print(pt.x, pt.y)
print(f"\n{pt.x}")
print(f"\n{pt.y}")

opera = namedtuple ('opera', ['name', 'composer', 'year'])
opera1 = opera('Turandot', 'Puccini', '1926')

#Accessing data items
print('Using index composer:' + opera1[1])
print('Using key composer:' + opera1.composer)

# 3. Ordered dictionaries - remembers or preserves the order of the keys that are inserted.

from collections import OrderedDict

order_dict = OrderedDict()
order_dict['a'] = 1
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['d'] = 4
print(f"\n{order_dict}")

order_dict = OrderedDict()
order_dict['b'] = 2
order_dict['c'] = 3
order_dict['d'] = 4
order_dict['a'] = 1
print(f"\n{order_dict}")

# 4. Default dictionary - A dictionary subclass that returns default values for missing keys.

from collections import defaultdict

def_dict = defaultdict(int) # can also be a float, list, tuple, or set.

def_dict['a'] = 1
def_dict['b'] = 2
def_dict['c'] = 3
def_dict['d'] = 4
print(f"\n{def_dict}")

print(f"\n{def_dict['a']}")
print(f"\n{def_dict['f']}") # returns int default value and returns an error for a normal dictionary.

dd = defaultdict(int)
words = str.split('data python structure data structure data python data structure')
for word in words:
    dd[word] += 1
print(f"\n{dd}")

# 5. deque - double ended que which be used to remove elements from both ends.

from collections import deque

d = deque()
d.append(1)
d.append(2)
print(f"{d}")

d.appendleft(3)
print(f"{d}")

# remove elements from the left side.
d.popleft()
print(f"{d}")

# remove elements from the right side.
d.pop()
print(f"{d}")

# extending a deque from the right 
d.extendleft([4, 5, 6])
print(f"{d}")

# extending a deque from the right 
d.extend([4, 5, 6])
print(f"{d}")

# rotate all elements one place to the left 
d.rotate(-1)
print(f"{d}")

# rotate all elements one place to the right 
d.rotate(1)
print(f"{d}")

# 6. ChainMap - used to create a list of dictionaries.

from collections import ChainMap

dict1 = {"mvano": 5, "cecilia": 2}
dict2 = {"python": 3, "opera": 10}

chain = ChainMap(dict1, dict2)
print(f"\n{chain}")

# get keys and values followed by converting them to lists.
print(f"\n{list(chain.keys())}")
print(list(chain.values()))

# search through all the dictionaries for the keys
print(f"\n{chain['mvano']}")
print(chain['opera'])