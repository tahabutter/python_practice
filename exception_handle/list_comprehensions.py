sqr = []

for i in range(10):
    sqr.append(i**2)
print(sqr)      

sqr =[i**2 for i in range(10)]
print(sqr)

sqr = [i**2 for i in range(10) if i % 2 != 0]
print(sqr)

val = [-2, -1, 0, 1, 2]
val = [0 if i < 0 else i for i in val]
print(val)

words = ["hello", "world", "python", "programming"]

words = [word.upper() for word in words]
print(words)