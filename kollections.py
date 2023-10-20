# U18A85519
# 1. Counter - This stores elements as dictionary keys and counts as dictionary values

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

# 2. nametuple

from collections import namedtuple

# create a class called Point with fields x and y
Point = namedtuple('Point', 'x,y')
pt = Point(2, 10)
print(f"\n{pt}")

#access the fields
print(f"\n{pt.x, pt.y}\n")
print(pt.x, pt.y)
print(f"\n{pt.x}")
print(f"\n{pt.y}")

# 3. OrderedDict - remembers the order at which the iterms where inserted

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

# 4. defaultdict - will have a default key-value pair if it has been not set yet.

from collections import defaultdict

def_dict = defaultdict(int) # can also be a float, list, tuple, or set.

def_dict['a'] = 1
def_dict['b'] = 2
def_dict['c'] = 3
def_dict['d'] = 4
print(f"\n{def_dict}")

print(f"\n{def_dict['a']}")
print(f"\n{def_dict['f']}") # returns int default value and returns an error for a normal dictionary.

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