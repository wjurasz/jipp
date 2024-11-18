from functools import reduce
print("reduce")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
numbers1 = reduce(lambda x,y: x if x > y else y, numbers)
print(numbers1)
b=10
print("------------------")
print("eval")
#eval transformuje tekst na kod wykonalny nie uzywamy na funkcjach wpisywanych z klawiatury
example = "2+2-b"
result = eval(example)
print(result)
print("------------------")
print("excec")
#
code = """
for i in range(3):
    print("witaj", i)
"""
exec(code)