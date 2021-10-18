from functools import reduce
ls =[12,32,42,13,42,24,15]
x = 0
def sum(ls):
    global x
    for num in ls:
        x+=num
    return x
print(sum(ls))
print("***** second method **********")
print(reduce(lambda y,z:y+z,ls))