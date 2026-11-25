import copy

a = [[1,2], [3,4]]

b = copy.copy(a)
c = copy.deepcopy(a)

print(a)
print(b)
print(c)

print(f"a is b = {a is b}")
print(f"a == b = {a == b}")

print(f"a is c = {a is c}")
print(f"a == c = {a == c}")