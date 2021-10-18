lst = [11,22,51,5,18,5,58,54,81,12]
'''ls =[]
def filter(lst):

    for item in lst:
        if item>50:
            ls.append(item)
        else:
            pass
    return ls
print(filter(lst))'''
print("using lambda function")
print(list(filter(lambda num:num>50,lst)))