def display(description, output):
    seperator = '=' * 10
    print()
    print(seperator)
    print(description)
    print("-" * 10)
    print(output)
    print(seperator)


a = {1, 2, 3}
b = {1, 2, 3, 4, 5, 6}

output = 'A {}\nB {}'.format(a, b)
display('SETS', output)

union = a | b
display('UNION', union)


intersection = a & b
display('INTERSECTION', intersection)

difference = a - b
display('A difference B', difference)

difference = b - a
display('B difference A', difference)

cartesian = set()
for _a in a:
    for _b in b:
        cartesian.add((_a, _b))

display('CARTESIAN', sorted(cartesian))

display('Is A a subsetof B', a.issubset(b))

display('Is B a subsetof A', b.issubset(a))
