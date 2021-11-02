# DemoLoop2.py

#list comprehension
lst = [1,2,3,4,5,6,7,8,9,10]
result = [i**2 for i in lst]
print(result)


d = {100:"apple", 200:"kiwi"}
print( [v.upper() for v in d.values()])